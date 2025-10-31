from abc import ABC, abstractmethod
from typing import Any, Callable, Optional
from collections import defaultdict
from enum import IntFlag, IntEnum
from hashlib import sha256
import struct
import time
import asyncio
import serial_asyncio
from .proto.companion import Companion as CompanionProto
from .proto.companion_cmds import CompanionCmds
from .proto.companion_common import CompanionCommon
from .proto.meshcore import Meshcore
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream
from kaitaistruct import BytesIO as KaitaiBytesIO
from dataclasses import dataclass, field, InitVar

DEFAULT_BAUD = 115200

class _Connection(ABC):
    @abstractmethod
    async def read_frame(self) -> bytes: ...

    @abstractmethod
    async def write_frame(self, data: bytes) -> None: ...

class SerialConnection(_Connection):
    def __init__(self, port: str, baud: int = DEFAULT_BAUD):
        self.port = port
        self.baud = baud
        self.reader = None
        self.writer = None

    async def connect(self) -> None:
        self.reader, self.writer = await serial_asyncio.open_serial_connection(
            url=self.port, 
            baudrate=self.baud
        )

    async def read_frame(self) -> bytes:
        text = b""
        while (c := await self.reader.read(1)) != b'>':
            text += c
        print(text.decode("utf-8"), end="")
        text = b""

        len, = struct.unpack("<H", await self.reader.readexactly(2))
        return await self.reader.readexactly(len)
    
    async def write_frame(self, data: bytes) -> None:
        self.writer.write(b'<' + struct.pack("<H", len(data)))
        self.writer.write(data)
        await self.writer.drain()

class NotConnected(Exception): pass

class _Device:
    def __init__(self, connection: _Connection = None):
        self.connection: Optional[_Connection] = connection
        self._on_start: list[Callable] = []

    def on_start(self, func):
        self._on_start.append(func)
        return func

    def _connection_required(self, func):
        def wrapper(self, *args, **kwargs):
            if not self.connection:
                raise NotConnected
            func(self, *args, **kwargs)
        return wrapper

    async def connect_serial(self, port: str, baud: int = DEFAULT_BAUD):
        conn = SerialConnection(port, baud)
        await conn.connect()
        self.connection = conn

    async def run_forever(self) -> None:
        await self._recv_loop()

    async def _recv_loop(self):
        raise NotImplementedError("Must be implemented in subclasses")

def _to_bytes(obj: ReadWriteKaitaiStruct, size: int) -> bytes:
    _io = KaitaiStream(KaitaiBytesIO(bytearray(size)))
    obj._write(_io)

    return _io.to_byte_array()

class Companion(_Device):
    Proto = CompanionProto

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_queue = asyncio.Queue()
        self.handlers: defaultdict[Any, list[Callable]] = defaultdict(list)
        self.handlers[id(CompanionProto.PushCode.new_advert)].append(self._on_new_advert)
        self._new_advert_handlers: list[Callable] = []
        self._msg_handlers: list[Callable] = []
        self._msg_waiting_handler = None
        self._seen_dms: set[int] = set()
        self._contacts_started = False
        self._contacts_handler = None

    class CompanionError(Exception): pass
    class CompanionErrorCode(Exception): pass
    class ContactsBusyException(Exception): pass
    class InvalidHashChannelName(Exception): pass

    class AdvertLocPolicy(IntEnum):
        None_ = 0
        Share = 1

    @dataclass
    class Contact:
        class Flags(IntFlag):
            Favourite = 0x01
            TelemPermBase = 0x02
            TelemPermLocation = 0x04
            TelemPermEnvironment = 0x08

        pub_key: bytes
        type: Meshcore.NodeType
        flags: Flags
        out_path: list[int]
        name: str
        last_advert_timestamp: int
        latitude: float
        longitude: float
        lastmod: float

    def _contact_from_payload(self, payload: CompanionProto.Contact | CompanionProto.NewAdvert):
        return Companion.Contact(
            payload.pub_key,
            payload.node_type,
            Companion.Contact.Flags.from_bytes(_to_bytes(payload.flags, 1)),
            payload.out_path[:payload.num_out_path] if payload.num_out_path != 0xFF else None,
            payload.name,
            payload.last_advert_timestamp,
            payload.latitude,
            payload.longitude,
            payload.lastmod
        )

    @dataclass
    class Message:

        companion: InitVar["Companion"]

        path_len: Optional[int]
        txt_type: CompanionCommon.TxtType
        sender_timestamp: int
        text: str

        def __post_init__(self, companion: "Companion"):
            self.companion = companion

        @abstractmethod
        async def reply(self, text: str):
            raise NotImplementedError("Must be implemented in subclasses")
            
    @dataclass
    class ContactMessage(Message):
        from_pub_key_prefix: bytes
        sender_prefix: bytes
        snr: Optional[float] = None

        async def reply(self, text: str):
            return await self.companion.send_txt_msg(self.from_pub_key_prefix, text)

    @dataclass
    class ChannelMessage(Message):
        channel_idx: int
        snr: Optional[float] = None

        async def reply(self, text: str):
            return await self.companion.send_channel_txt_msg(self.channel_idx, text)

    def _msg_from_payload(self, payload: ReadWriteKaitaiStruct):
        snr = None
        if isinstance(payload, CompanionProto.ContactMsgRecvV3) or isinstance(payload, CompanionProto.ChannelMsgRecvV3):
            snr = payload.snr
            payload = payload.message

        if isinstance(payload, CompanionProto.ContactMsgRecv):
            return Companion.ContactMessage(
                self,
                payload.path_len if payload.is_flood else None,
                CompanionCommon.TxtType(payload.txt_type),
                payload.sender_timestamp,
                payload.text,
                payload.from_pub_key_prefix,
                payload.sender_prefix if payload.txt_type == CompanionCommon.TxtType.signed_plain else None,
                snr
            )
        elif isinstance(payload, CompanionProto.ChannelMsgRecv):
            return Companion.ChannelMessage(
                self,
                payload.path_len if payload.is_flood else None,
                payload.txt_type,
                payload.sender_timestamp,
                payload.text,
                payload.channel_idx,
                snr
            )
        assert False

    @dataclass
    class Channel:
        name: str
        secret: bytes

        def from_hashtag(name: str):
            if name[0] != '#':
                raise Companion.InvalidHashChannelName()
            for c in name[1:]:
                if c not in "abcdefghijklmnopqrstuvwxyz0123456789-":
                    raise Companion.InvalidHashChannelName()
            sha256sum = sha256(name.encode("utf-8")).digest()
            return Companion.Channel(name, sha256sum[:16])
        
    PUBLIC_CHANNEL = Channel("Public", bytes.fromhex("8b3387e9c5cdea6ac9e5edbaa115cd72"))

    def _channel_from_payload(self, payload: CompanionProto.ChannelInfo):
        return Companion.Channel(
            payload.name,
            payload.secret
        )
    
    async def _msg_handler(self):
        code, payload = await self.sync_next_message()
        assert code in (CompanionProto.RespCode.channel_msg_recv, CompanionProto.RespCode.channel_msg_recv_v3, CompanionProto.RespCode.contact_msg_recv, CompanionProto.RespCode.contact_msg_recv_v3)

        msg = self._msg_from_payload(payload)

        if isinstance(msg, Companion.ContactMessage):
            msg_hash = hash((msg.txt_type, msg.sender_timestamp, msg.text, msg.from_pub_key_prefix, msg.sender_prefix))
            if msg_hash in self._seen_dms:
                return
            self._seen_dms.add(msg_hash)
        
        for handler in self._msg_handlers:
            await handler(msg)
    
    async def sync_messages(self):
        if self._msg_waiting_handler is not None: return
        while True:
            code, payload = await self.sync_next_message()
            if code == CompanionProto.RespCode.no_more_messages:
                self._msg_waiting_handler = self._msg_handler
                break

            for handler in self._msg_handlers:
                await handler(self._msg_from_payload(payload))
    
    def on(self, on: Any):
        def decorator(func: Callable):
            # id is used to differentiate between enums of the same value but different type
            self.handlers[id(on)].append(func)
            return func
        return decorator
    
    def on_msg(self, func):
        self._msg_handlers.append(func)
        return func
    
    def on_new_advert(self, func):
        self._new_advert_handlers.append(func)
        return func
    
    async def _on_new_advert(self, payload: CompanionProto.NewAdvert):
        contact = self._contact_from_payload(payload)
        for handler in self._new_advert_handlers:
            await handler(contact)

    @staticmethod
    def _begin_command(command: CompanionCmds.Command):
        data = CompanionCmds()
        data.command = command
        return None, data, data._root
    
    async def _finalise_send_command(self, payload: Optional[tuple[ReadWriteKaitaiStruct, int]] = None, data: Optional[tuple[Any, ReadWriteKaitaiStruct, Any]] = None) -> tuple[CompanionProto.RespCode, Optional[ReadWriteKaitaiStruct]]:
        payload_len = 0
        if payload is not None:
            _payload, payload_len = payload
            _data = _payload._root
            _payload._check()
            _data.payload = _payload
        else:
            _data = data[1]
        _data._check()
        future = asyncio.get_running_loop().create_future()
        await self.task_queue.put(future)
        await self.connection.write_frame(_to_bytes(_data, 1 + payload_len))
        return await future

    async def app_start(self, app_name: str = "PyMeshCore"):
        payload = CompanionCmds.AppStart(*self._begin_command(CompanionCmds.Command.app_start))
        payload.reserved = b"\x00" * 7
        payload.app_name = app_name
        return await self._finalise_send_command((payload, 7 + len(app_name.encode("utf-8"))))

    async def send_txt_msg(self, pub_key_prefix: bytes, text: str, attempt: int = 0, txt_type: CompanionCommon.TxtType = CompanionCommon.TxtType.plain, timestamp: Optional[int] = None):
        if timestamp is None:
            timestamp = int(time.time())

        payload = CompanionCmds.SendTxtMsg(*self._begin_command(CompanionCmds.Command.send_txt_msg))
        payload.txt_type = txt_type
        payload.attempt = attempt
        payload.msg_timestamp = timestamp
        payload.pub_key_prefix = pub_key_prefix
        payload.text = text
        return await self._finalise_send_command((payload, 1 + 1 + 4 + 6 + len(text.encode("utf-8"))))
    
    async def send_channel_txt_msg(self, channel_idx: int, text: str, txt_type: CompanionCommon.TxtType = CompanionCommon.TxtType.plain, timestamp: Optional[int] = None):
        if timestamp is None:
            timestamp = int(time.time())

        payload = CompanionCmds.SendChannelTxtMsg(*self._begin_command(CompanionCmds.Command.send_channel_txt_msg))
        payload.txt_type = txt_type
        payload.channel_idx = channel_idx
        payload.msg_timestamp = timestamp
        payload.text = text
        return await self._finalise_send_command((payload, 1 + 1 + 4 + len(text.encode("utf-8"))))
    
    async def send_self_advert(self, flood: bool):
        payload = CompanionCmds.SendSelfAdvert(*self._begin_command(CompanionCmds.Command.send_self_advert))
        payload.flood = int(flood)
        return await self._finalise_send_command((payload, 1))
    
    async def set_advert_name(self, name: str):
        payload = CompanionCmds.SetAdvertName(*self._begin_command(CompanionCmds.Command.set_advert_name))
        payload.name = name
        return await self._finalise_send_command((payload, len(name.encode("utf-8"))))
    
    async def add_update_contact(self, contact: Contact):
        payload = CompanionCmds.AddUpdateContact(*self._begin_command(CompanionCmds.Command.add_update_contact))
        payload.pub_key = contact.pub_key
        payload.type = contact.type.value
        flags = CompanionCommon.ContactFlags(KaitaiStream(KaitaiBytesIO(contact.flags.to_bytes())), payload, payload._root)
        flags._read()
        flags._check()
        payload.flags = flags
        if contact.out_path is not None:
            payload.num_out_path = len(contact.out_path)
            payload.out_path = contact.out_path + [0] * (64 - len(contact.out_path))
        else:
            payload.num_out_path = 0xFF
            payload.out_path = [0] * 64
        payload.name = contact.name
        payload.last_advert_timestamp = contact.last_advert_timestamp

        location = CompanionCmds.AddUpdateContactLoc(None, payload, payload._root)
        location.latitude_microdegrees = int(round(contact.latitude * 1000000)) if contact.latitude is not None else 0
        location.longitude_microdegrees = int(round(contact.longitude * 1000000)) if contact.longitude is not None else 0
        location._check()
        payload.location = location
        payload.lastmod = contact.lastmod
        return await self._finalise_send_command((payload, 32 + 1 + 1 + 1 + 64 + 32 + 4 + 8 + 4))

    async def sync_next_message(self):
        return await self._finalise_send_command(data=self._begin_command(CompanionCmds.Command.sync_next_message))

    async def set_radio_tx_power(self, tx_power: int):
        payload = CompanionCmds.SetRadioTxPower(*self._begin_command(CompanionCmds.Command.set_radio_tx_power))
        payload.tx_power = tx_power
        return await self._finalise_send_command((payload, 1))

    async def device_query(self, app_target_ver: int = 3):
        payload = CompanionCmds.DeviceQuery(*self._begin_command(CompanionCmds.Command.device_query))
        payload.app_target_ver = app_target_ver
        return await self._finalise_send_command((payload, 1))
    
    async def _get_contacts(self, since: int = 0):
        payload = CompanionCmds.GetContacts(*self._begin_command(CompanionCmds.Command.get_contacts))
        payload.since = since
        return await self._finalise_send_command((payload, 1 + 4))
    
    async def get_contacts(self, since: Optional[int] = 0) -> tuple[list[Contact], int]:
        if self._contacts_handler is not None:
            raise Companion.ContactsBusyException()

        done = asyncio.get_running_loop().create_future()
        contacts = []
        async def on_contact(payload: CompanionProto.Contact | CompanionProto.EndOfContacts):
            if isinstance(payload, CompanionProto.EndOfContacts):
                done.set_result(payload.lastmod)
                self._contacts_handler = None
                self._contacts_started = False
                return
            
            contacts.append(self._contact_from_payload(payload))

        self._contacts_handler = on_contact
        code, payload = await self._get_contacts(since)
        if code != CompanionProto.RespCode.contacts_start:
            self._contacts_handler = None
            raise Companion.CompanionError(code, payload)
        
        lastmod = await done
        return contacts, lastmod
        
    async def remove_contact(self, public_key: bytes):
        payload = CompanionCmds.PubKeyPayload(*self._begin_command(CompanionCmds.Command.remove_contact))
        payload.pub_key = public_key
        return await self._finalise_send_command((payload, 32))
    
    async def _get_channel(self, channel_idx: int):
        payload = CompanionCmds.GetChannel(*self._begin_command(CompanionCmds.Command.get_channel))
        payload.channel_idx = channel_idx
        return await self._finalise_send_command((payload, 1))
    
    async def get_channel(self, channel_idx: int):
        code, payload = await self._get_channel(channel_idx)
        if code == CompanionProto.RespCode.err:
            payload: CompanionProto.Err
            raise Companion.CompanionErrorCode(payload.err_code)
        assert code == CompanionProto.RespCode.channel_info
        return self._channel_from_payload(payload)
    
    async def get_channels(self, count: int) -> list[Optional[Channel]]:
        channels = []
        for i in range(count):
            try:
                channel = await self.get_channel(i)
            except Companion.CompanionErrorCode as e:
                if e.args == CompanionProto.ErrCode.not_found:
                    break
                raise
            if channel.name == "" and channel.secret == b"\x00" * 16:
                channels.append(None)
            else:
                channels.append(channel)
        return channels
    
    async def set_channel(self, channel_idx: int, channel: Channel):
        payload = CompanionCmds.SetChannel(*self._begin_command(CompanionCmds.Command.set_channel))
        payload.channel_idx = channel_idx
        payload.channel_name = channel.name
        payload.channel_secret = channel.secret
        return await self._finalise_send_command((payload, 1 + 32 + 16))
    
    async def set_other_params(self, manual_add_contacts: bool, telem_mode_base: Optional[bool] = None, telem_mode_loc: Optional[bool] = None, telem_mode_env: Optional[bool] = None, multi_acks: Optional[int] = None, advert_loc_policy: Optional[AdvertLocPolicy] = None):
        payload = CompanionCmds.SetOtherParams(*self._begin_command(CompanionCmds.Command.set_other_params))
        payload.manual_add_contacts = manual_add_contacts
        if None not in (telem_mode_base, telem_mode_loc, telem_mode_env):
            telemetry = CompanionCmds.SetOtherParamsTelemetry(None, payload, payload._root)
            telemetry.telemetry_mode_base = telem_mode_base
            telemetry.telemetry_mode_loc = telem_mode_loc
            telemetry.telemetry_mode_env = telem_mode_env
            telemetry._check()
            payload.telemetry = telemetry
            if multi_acks is not None:
                payload.multi_acks = multi_acks
                if advert_loc_policy is not None:
                    payload.advert_loc_policy = advert_loc_policy.value
        return await self._finalise_send_command((payload, 1))

    async def _recv_loop(self):
        self._msg_waiting_handler = None
        for handler in self._on_start:
            asyncio.create_task(handler())
        while True:
            frame = await self.connection.read_frame()
            data = CompanionProto.from_bytes(frame)
            data._read()
            if data.is_push:
                code = data.push_code
                payload = getattr(data, "push_payload", None)
                if code == CompanionProto.PushCode.msg_waiting and self._msg_waiting_handler is not None:
                    asyncio.create_task(self._msg_waiting_handler())
            else:
                code = data.resp_code
                payload = getattr(data, "resp_payload", None)
                if self._contacts_started:
                    await self._contacts_handler(payload)
                else:
                    future: asyncio.Future = self.task_queue.get_nowait()
                    future.set_result((code, payload))
                if code == CompanionProto.RespCode.contacts_start:
                    self._contacts_started = True
            for handler in self.handlers[id(code)]:
                asyncio.create_task(handler(payload))
