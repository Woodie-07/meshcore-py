# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from . import companion_common
from . import meshcore
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Companion(ReadWriteKaitaiStruct):

    class ErrCode(IntEnum):
        unsupported_cmd = 1
        not_found = 2
        table_full = 3
        bad_state = 4
        file_io_error = 5
        illegal_arg = 6

    class PushCode(IntEnum):
        advert = 0
        path_updated = 1
        send_confirmed = 2
        msg_waiting = 3
        raw_data = 4
        login_success = 5
        login_fail = 6
        status_response = 7
        log_rx_data = 8
        trace_data = 9
        new_advert = 10
        telemetry_response = 11
        binary_response = 12
        path_discovery_response = 13

    class RespCode(IntEnum):
        ok = 0
        err = 1
        contacts_start = 2
        contact = 3
        end_of_contacts = 4
        self_info = 5
        sent = 6
        contact_msg_recv = 7
        channel_msg_recv = 8
        curr_time = 9
        no_more_messages = 10
        export_contact = 11
        batt_and_storage = 12
        device_info = 13
        private_key = 14
        disabled = 15
        contact_msg_recv_v3 = 16
        channel_msg_recv_v3 = 17
        channel_info = 18
        sign_start = 19
        signature = 20
        custom_vars = 21
        advert_path = 22
        tuning_params = 23
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Companion, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.is_push = self._io.read_bits_int_be(1) != 0
        if (not (self.is_push)):
            pass
            self.resp_code = KaitaiStream.resolve_enum(Companion.RespCode, self._io.read_bits_int_be(7))

        if self.is_push:
            pass
            self.push_code = KaitaiStream.resolve_enum(Companion.PushCode, self._io.read_bits_int_be(7))

        if (not (self.is_push)):
            pass
            _on = self.resp_code
            if _on == Companion.RespCode.channel_info:
                pass
                self.resp_payload = Companion.ChannelInfo(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.channel_msg_recv:
                pass
                self.resp_payload = Companion.ChannelMsgRecv(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.channel_msg_recv_v3:
                pass
                self.resp_payload = Companion.ChannelMsgRecvV3(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.contact:
                pass
                self.resp_payload = Companion.Contact(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.contact_msg_recv:
                pass
                self.resp_payload = Companion.ContactMsgRecv(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.contact_msg_recv_v3:
                pass
                self.resp_payload = Companion.ContactMsgRecvV3(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.contacts_start:
                pass
                self.resp_payload = Companion.ContactsStart(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.curr_time:
                pass
                self.resp_payload = Companion.CurrTime(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.device_info:
                pass
                self.resp_payload = Companion.DeviceInfo(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.end_of_contacts:
                pass
                self.resp_payload = Companion.EndOfContacts(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.err:
                pass
                self.resp_payload = Companion.Err(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.private_key:
                pass
                self.resp_payload = Companion.PrivateKey(self._io, self, self._root)
                self.resp_payload._read()
            elif _on == Companion.RespCode.self_info:
                pass
                self.resp_payload = Companion.SelfInfo(self._io, self, self._root)
                self.resp_payload._read()

        if self.is_push:
            pass
            _on = self.push_code
            if _on == Companion.PushCode.advert:
                pass
                self.push_payload = Companion.PubKeyPayload(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.binary_response:
                pass
                self.push_payload = Companion.BinaryResponse(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.log_rx_data:
                pass
                self.push_payload = Companion.LogRxData(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.login_fail:
                pass
                self.push_payload = Companion.LoginFail(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.login_success:
                pass
                self.push_payload = Companion.LoginSuccess(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.new_advert:
                pass
                self.push_payload = Companion.NewAdvert(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.path_discovery_response:
                pass
                self.push_payload = Companion.PathDiscoveryResponse(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.path_updated:
                pass
                self.push_payload = Companion.PubKeyPayload(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.raw_data:
                pass
                self.push_payload = Companion.RawData(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.send_confirmed:
                pass
                self.push_payload = Companion.SendConfirmed(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.status_response:
                pass
                self.push_payload = Companion.StatusResponse(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.telemetry_response:
                pass
                self.push_payload = Companion.TelemetryResponse(self._io, self, self._root)
                self.push_payload._read()
            elif _on == Companion.PushCode.trace_data:
                pass
                self.push_payload = Companion.TraceData(self._io, self, self._root)
                self.push_payload._read()

        self._dirty = False


    def _fetch_instances(self):
        pass
        if (not (self.is_push)):
            pass

        if self.is_push:
            pass

        if (not (self.is_push)):
            pass
            _on = self.resp_code
            if _on == Companion.RespCode.channel_info:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.channel_msg_recv:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.channel_msg_recv_v3:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.contact:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.contact_msg_recv:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.contact_msg_recv_v3:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.contacts_start:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.curr_time:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.device_info:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.end_of_contacts:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.err:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.private_key:
                pass
                self.resp_payload._fetch_instances()
            elif _on == Companion.RespCode.self_info:
                pass
                self.resp_payload._fetch_instances()

        if self.is_push:
            pass
            _on = self.push_code
            if _on == Companion.PushCode.advert:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.binary_response:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.log_rx_data:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.login_fail:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.login_success:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.new_advert:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.path_discovery_response:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.path_updated:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.raw_data:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.send_confirmed:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.status_response:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.telemetry_response:
                pass
                self.push_payload._fetch_instances()
            elif _on == Companion.PushCode.trace_data:
                pass
                self.push_payload._fetch_instances()



    def _write__seq(self, io=None):
        super(Companion, self)._write__seq(io)
        self._io.write_bits_int_be(1, int(self.is_push))
        if (not (self.is_push)):
            pass
            self._io.write_bits_int_be(7, int(self.resp_code))

        if self.is_push:
            pass
            self._io.write_bits_int_be(7, int(self.push_code))

        if (not (self.is_push)):
            pass
            _on = self.resp_code
            if _on == Companion.RespCode.channel_info:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.channel_msg_recv:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.channel_msg_recv_v3:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.contact:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.contact_msg_recv:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.contact_msg_recv_v3:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.contacts_start:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.curr_time:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.device_info:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.end_of_contacts:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.err:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.private_key:
                pass
                self.resp_payload._write__seq(self._io)
            elif _on == Companion.RespCode.self_info:
                pass
                self.resp_payload._write__seq(self._io)

        if self.is_push:
            pass
            _on = self.push_code
            if _on == Companion.PushCode.advert:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.binary_response:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.log_rx_data:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.login_fail:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.login_success:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.new_advert:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.path_discovery_response:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.path_updated:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.raw_data:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.send_confirmed:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.status_response:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.telemetry_response:
                pass
                self.push_payload._write__seq(self._io)
            elif _on == Companion.PushCode.trace_data:
                pass
                self.push_payload._write__seq(self._io)



    def _check(self):
        if (not (self.is_push)):
            pass

        if self.is_push:
            pass

        if (not (self.is_push)):
            pass
            _on = self.resp_code
            if _on == Companion.RespCode.channel_info:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.channel_msg_recv:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.channel_msg_recv_v3:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.contact:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.contact_msg_recv:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.contact_msg_recv_v3:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.contacts_start:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.curr_time:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.device_info:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.end_of_contacts:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.err:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.private_key:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)
            elif _on == Companion.RespCode.self_info:
                pass
                if self.resp_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self._root, self.resp_payload._root)
                if self.resp_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"resp_payload", self, self.resp_payload._parent)

        if self.is_push:
            pass
            _on = self.push_code
            if _on == Companion.PushCode.advert:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.binary_response:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.log_rx_data:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.login_fail:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.login_success:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.new_advert:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.path_discovery_response:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.path_updated:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.raw_data:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.send_confirmed:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.status_response:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.telemetry_response:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)
            elif _on == Companion.PushCode.trace_data:
                pass
                if self.push_payload._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self._root, self.push_payload._root)
                if self.push_payload._parent != self:
                    raise kaitaistruct.ConsistencyError(u"push_payload", self, self.push_payload._parent)

        self._dirty = False

    class BinaryResponse(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.BinaryResponse, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.tag = self._io.read_u4le()
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.BinaryResponse, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_u4le(self.tag)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class ChannelInfo(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ChannelInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.index = self._io.read_u1()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self.secret = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.ChannelInfo, self)._write__seq(io)
            self._io.write_u1(self.index)
            self._io.write_bytes_limit((self.name).encode(u"UTF-8"), 32, 0, 0)
            self._io.write_bytes(self.secret)


        def _check(self):
            if len((self.name).encode(u"UTF-8")) > 32:
                raise kaitaistruct.ConsistencyError(u"name", 32, len((self.name).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"name", -1, KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0))
            if len(self.secret) != 16:
                raise kaitaistruct.ConsistencyError(u"secret", 16, len(self.secret))
            self._dirty = False


    class ChannelMsgRecv(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ChannelMsgRecv, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.channel_idx = self._io.read_u1()
            self.path_len = self._io.read_u1()
            self.txt_type = KaitaiStream.resolve_enum(companion_common.CompanionCommon.TxtType, self._io.read_u1())
            self.sender_timestamp = self._io.read_u4le()
            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.ChannelMsgRecv, self)._write__seq(io)
            self._io.write_u1(self.channel_idx)
            self._io.write_u1(self.path_len)
            self._io.write_u1(int(self.txt_type))
            self._io.write_u4le(self.sender_timestamp)
            self._io.write_bytes((self.text).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"text", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def is_flood(self):
            if hasattr(self, '_m_is_flood'):
                return self._m_is_flood

            self._m_is_flood = self.path_len != 255
            return getattr(self, '_m_is_flood', None)

        def _invalidate_is_flood(self):
            del self._m_is_flood

    class ChannelMsgRecvV3(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ChannelMsgRecvV3, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.snr_raw = self._io.read_s1()
            self.reserved1 = self._io.read_u1()
            self.reserved2 = self._io.read_u1()
            self.message = Companion.ChannelMsgRecv(self._io, self, self._root)
            self.message._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.message._fetch_instances()


        def _write__seq(self, io=None):
            super(Companion.ChannelMsgRecvV3, self)._write__seq(io)
            self._io.write_s1(self.snr_raw)
            self._io.write_u1(self.reserved1)
            self._io.write_u1(self.reserved2)
            self.message._write__seq(self._io)


        def _check(self):
            if self.message._root != self._root:
                raise kaitaistruct.ConsistencyError(u"message", self._root, self.message._root)
            if self.message._parent != self:
                raise kaitaistruct.ConsistencyError(u"message", self, self.message._parent)
            self._dirty = False

        @property
        def snr(self):
            if hasattr(self, '_m_snr'):
                return self._m_snr

            self._m_snr = self.snr_raw / 4.0
            return getattr(self, '_m_snr', None)

        def _invalidate_snr(self):
            del self._m_snr

    class Contact(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.Contact, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self.node_type = KaitaiStream.resolve_enum(meshcore.Meshcore.NodeType, self._io.read_u1())
            self.flags = companion_common.CompanionCommon.ContactFlags(self._io)
            self.flags._read()
            self.num_out_path = self._io.read_u1()
            self.out_path = []
            for i in range(64):
                self.out_path.append(self._io.read_u1())

            self.name = KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)
            self.last_advert_timestamp = self._io.read_u4le()
            self.latitude_microdegrees = self._io.read_u4le()
            self.longitude_microdegrees = self._io.read_u4le()
            self.lastmod = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()
            for i in range(len(self.out_path)):
                pass



        def _write__seq(self, io=None):
            super(Companion.Contact, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)
            self._io.write_u1(int(self.node_type))
            self.flags._write__seq(self._io)
            self._io.write_u1(self.num_out_path)
            for i in range(len(self.out_path)):
                pass
                self._io.write_u1(self.out_path[i])

            self._io.write_bytes_limit(self.name, 32, 0, 0)
            self._io.write_u4le(self.last_advert_timestamp)
            self._io.write_u4le(self.latitude_microdegrees)
            self._io.write_u4le(self.longitude_microdegrees)
            self._io.write_u4le(self.lastmod)


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            if len(self.out_path) != 64:
                raise kaitaistruct.ConsistencyError(u"out_path", 64, len(self.out_path))
            for i in range(len(self.out_path)):
                pass

            if len(self.name) > 32:
                raise kaitaistruct.ConsistencyError(u"name", 32, len(self.name))
            if KaitaiStream.byte_array_index_of(self.name, 0) != -1:
                raise kaitaistruct.ConsistencyError(u"name", -1, KaitaiStream.byte_array_index_of(self.name, 0))
            self._dirty = False

        @property
        def has_out_path(self):
            if hasattr(self, '_m_has_out_path'):
                return self._m_has_out_path

            self._m_has_out_path = self.num_out_path != 255
            return getattr(self, '_m_has_out_path', None)

        def _invalidate_has_out_path(self):
            del self._m_has_out_path
        @property
        def latitude(self):
            if hasattr(self, '_m_latitude'):
                return self._m_latitude

            self._m_latitude = self.latitude_microdegrees / 1000000.0
            return getattr(self, '_m_latitude', None)

        def _invalidate_latitude(self):
            del self._m_latitude
        @property
        def longitude(self):
            if hasattr(self, '_m_longitude'):
                return self._m_longitude

            self._m_longitude = self.longitude_microdegrees / 1000000.0
            return getattr(self, '_m_longitude', None)

        def _invalidate_longitude(self):
            del self._m_longitude

    class ContactMsgRecv(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ContactMsgRecv, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.from_pub_key_prefix = self._io.read_bytes(6)
            self.path_len = self._io.read_u1()
            self.txt_type = KaitaiStream.resolve_enum(companion_common.CompanionCommon.TxtType, self._io.read_u1())
            self.sender_timestamp = self._io.read_u4le()
            if self.txt_type == companion_common.CompanionCommon.TxtType.signed_plain:
                pass
                self.sender_prefix = self._io.read_bytes(4)

            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass
            if self.txt_type == companion_common.CompanionCommon.TxtType.signed_plain:
                pass



        def _write__seq(self, io=None):
            super(Companion.ContactMsgRecv, self)._write__seq(io)
            self._io.write_bytes(self.from_pub_key_prefix)
            self._io.write_u1(self.path_len)
            self._io.write_u1(int(self.txt_type))
            self._io.write_u4le(self.sender_timestamp)
            if self.txt_type == companion_common.CompanionCommon.TxtType.signed_plain:
                pass
                self._io.write_bytes(self.sender_prefix)

            self._io.write_bytes((self.text).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"text", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.from_pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"from_pub_key_prefix", 6, len(self.from_pub_key_prefix))
            if self.txt_type == companion_common.CompanionCommon.TxtType.signed_plain:
                pass
                if len(self.sender_prefix) != 4:
                    raise kaitaistruct.ConsistencyError(u"sender_prefix", 4, len(self.sender_prefix))

            self._dirty = False

        @property
        def is_flood(self):
            if hasattr(self, '_m_is_flood'):
                return self._m_is_flood

            self._m_is_flood = self.path_len != 255
            return getattr(self, '_m_is_flood', None)

        def _invalidate_is_flood(self):
            del self._m_is_flood

    class ContactMsgRecvV3(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ContactMsgRecvV3, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.snr_raw = self._io.read_s1()
            self.reserved1 = self._io.read_u1()
            self.reserved2 = self._io.read_u1()
            self.message = Companion.ContactMsgRecv(self._io, self, self._root)
            self.message._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.message._fetch_instances()


        def _write__seq(self, io=None):
            super(Companion.ContactMsgRecvV3, self)._write__seq(io)
            self._io.write_s1(self.snr_raw)
            self._io.write_u1(self.reserved1)
            self._io.write_u1(self.reserved2)
            self.message._write__seq(self._io)


        def _check(self):
            if self.message._root != self._root:
                raise kaitaistruct.ConsistencyError(u"message", self._root, self.message._root)
            if self.message._parent != self:
                raise kaitaistruct.ConsistencyError(u"message", self, self.message._parent)
            self._dirty = False

        @property
        def snr(self):
            if hasattr(self, '_m_snr'):
                return self._m_snr

            self._m_snr = self.snr_raw / 4.0
            return getattr(self, '_m_snr', None)

        def _invalidate_snr(self):
            del self._m_snr

    class ContactsStart(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.ContactsStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_contacts = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.ContactsStart, self)._write__seq(io)
            self._io.write_u4le(self.num_contacts)


        def _check(self):
            self._dirty = False


    class CurrTime(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.CurrTime, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.secs = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.CurrTime, self)._write__seq(io)
            self._io.write_u4le(self.secs)


        def _check(self):
            self._dirty = False


    class DeviceInfo(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.DeviceInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.firmware_ver_code = self._io.read_u1()
            self.max_contacts_raw = self._io.read_u1()
            self.max_group_channels = self._io.read_u1()
            self.ble_pin = self._io.read_u4le()
            self.firmware_build_date = (KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)).decode(u"UTF-8")
            self.board_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"UTF-8")
            self.firmware_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(20), 0, False)).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.DeviceInfo, self)._write__seq(io)
            self._io.write_u1(self.firmware_ver_code)
            self._io.write_u1(self.max_contacts_raw)
            self._io.write_u1(self.max_group_channels)
            self._io.write_u4le(self.ble_pin)
            self._io.write_bytes_limit((self.firmware_build_date).encode(u"UTF-8"), 12, 0, 0)
            self._io.write_bytes_limit((self.board_name).encode(u"UTF-8"), 40, 0, 0)
            self._io.write_bytes_limit((self.firmware_version).encode(u"UTF-8"), 20, 0, 0)


        def _check(self):
            if len((self.firmware_build_date).encode(u"UTF-8")) > 12:
                raise kaitaistruct.ConsistencyError(u"firmware_build_date", 12, len((self.firmware_build_date).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.firmware_build_date).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"firmware_build_date", -1, KaitaiStream.byte_array_index_of((self.firmware_build_date).encode(u"UTF-8"), 0))
            if len((self.board_name).encode(u"UTF-8")) > 40:
                raise kaitaistruct.ConsistencyError(u"board_name", 40, len((self.board_name).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.board_name).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"board_name", -1, KaitaiStream.byte_array_index_of((self.board_name).encode(u"UTF-8"), 0))
            if len((self.firmware_version).encode(u"UTF-8")) > 20:
                raise kaitaistruct.ConsistencyError(u"firmware_version", 20, len((self.firmware_version).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.firmware_version).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"firmware_version", -1, KaitaiStream.byte_array_index_of((self.firmware_version).encode(u"UTF-8"), 0))
            self._dirty = False

        @property
        def max_contacts(self):
            if hasattr(self, '_m_max_contacts'):
                return self._m_max_contacts

            self._m_max_contacts = self.max_contacts_raw * 2
            return getattr(self, '_m_max_contacts', None)

        def _invalidate_max_contacts(self):
            del self._m_max_contacts

    class EndOfContacts(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.EndOfContacts, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.lastmod = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.EndOfContacts, self)._write__seq(io)
            self._io.write_u4le(self.lastmod)


        def _check(self):
            self._dirty = False


    class Err(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.Err, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.err_code = KaitaiStream.resolve_enum(Companion.ErrCode, self._io.read_u1())
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.Err, self)._write__seq(io)
            self._io.write_u1(int(self.err_code))


        def _check(self):
            self._dirty = False


    class LogRxData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.LogRxData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.snr_raw = self._io.read_s1()
            self.rssi = self._io.read_s1()
            self.packet = meshcore.Meshcore(self._io)
            self.packet._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.packet._fetch_instances()


        def _write__seq(self, io=None):
            super(Companion.LogRxData, self)._write__seq(io)
            self._io.write_s1(self.snr_raw)
            self._io.write_s1(self.rssi)
            self.packet._write__seq(self._io)


        def _check(self):
            self._dirty = False

        @property
        def snr(self):
            if hasattr(self, '_m_snr'):
                return self._m_snr

            self._m_snr = self.snr_raw / 4.0
            return getattr(self, '_m_snr', None)

        def _invalidate_snr(self):
            del self._m_snr

    class Login(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.Login, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key_prefix = self._io.read_bytes(6)
            self.tag = self._io.read_u4le()
            self.acl_permissions = self._io.read_u1()
            self.firmware_ver_level = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.Login, self)._write__seq(io)
            self._io.write_bytes(self.pub_key_prefix)
            self._io.write_u4le(self.tag)
            self._io.write_u1(self.acl_permissions)
            self._io.write_u1(self.firmware_ver_level)


        def _check(self):
            if len(self.pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"pub_key_prefix", 6, len(self.pub_key_prefix))
            self._dirty = False


    class LoginFail(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.LoginFail, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.LoginFail, self)._write__seq(io)
            self._io.write_u1(self.reserved)


        def _check(self):
            self._dirty = False


    class LoginSuccess(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.LoginSuccess, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.permissions = self._io.read_u1()
            if (not (self._io.is_eof())):
                pass
                self.login = Companion.Login(self._io, self, self._root)
                self.login._read()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass
                self.login._fetch_instances()



        def _write__seq(self, io=None):
            super(Companion.LoginSuccess, self)._write__seq(io)
            self._io.write_u1(self.permissions)
            if (not (self._io.is_eof())):
                pass
                if self.login._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"login", self._root, self.login._root)
                if self.login._parent != self:
                    raise kaitaistruct.ConsistencyError(u"login", self, self.login._parent)
                self.login._write__seq(self._io)



        def _check(self):
            self._dirty = False


    class NewAdvert(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.NewAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self.node_type = KaitaiStream.resolve_enum(meshcore.Meshcore.NodeType, self._io.read_u1())
            self.flags = companion_common.CompanionCommon.ContactFlags(self._io)
            self.flags._read()
            self.num_out_path = self._io.read_u1()
            self.out_path = []
            for i in range(64):
                self.out_path.append(self._io.read_u1())

            self.name = KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)
            self.last_advert_timestamp = self._io.read_u4le()
            self.latitude_microdegrees = self._io.read_u4le()
            self.longitude_microdegrees = self._io.read_u4le()
            self.lastmod = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()
            for i in range(len(self.out_path)):
                pass



        def _write__seq(self, io=None):
            super(Companion.NewAdvert, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)
            self._io.write_u1(int(self.node_type))
            self.flags._write__seq(self._io)
            self._io.write_u1(self.num_out_path)
            for i in range(len(self.out_path)):
                pass
                self._io.write_u1(self.out_path[i])

            self._io.write_bytes_limit(self.name, 32, 0, 0)
            self._io.write_u4le(self.last_advert_timestamp)
            self._io.write_u4le(self.latitude_microdegrees)
            self._io.write_u4le(self.longitude_microdegrees)
            self._io.write_u4le(self.lastmod)


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            if len(self.out_path) != 64:
                raise kaitaistruct.ConsistencyError(u"out_path", 64, len(self.out_path))
            for i in range(len(self.out_path)):
                pass

            if len(self.name) > 32:
                raise kaitaistruct.ConsistencyError(u"name", 32, len(self.name))
            if KaitaiStream.byte_array_index_of(self.name, 0) != -1:
                raise kaitaistruct.ConsistencyError(u"name", -1, KaitaiStream.byte_array_index_of(self.name, 0))
            self._dirty = False

        @property
        def latitude(self):
            if hasattr(self, '_m_latitude'):
                return self._m_latitude

            self._m_latitude = self.latitude_microdegrees / 1000000.0
            return getattr(self, '_m_latitude', None)

        def _invalidate_latitude(self):
            del self._m_latitude
        @property
        def longitude(self):
            if hasattr(self, '_m_longitude'):
                return self._m_longitude

            self._m_longitude = self.longitude_microdegrees / 1000000.0
            return getattr(self, '_m_longitude', None)

        def _invalidate_longitude(self):
            del self._m_longitude

    class PathDiscoveryResponse(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.PathDiscoveryResponse, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.pub_key_prefix = self._io.read_bytes(6)
            self.num_out_path = self._io.read_u1()
            self.out_path = []
            for i in range(self.num_out_path):
                self.out_path.append(self._io.read_u1())

            self.num_in_path = self._io.read_u1()
            self.in_path = []
            for i in range(self.num_in_path):
                self.in_path.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.out_path)):
                pass

            for i in range(len(self.in_path)):
                pass



        def _write__seq(self, io=None):
            super(Companion.PathDiscoveryResponse, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.pub_key_prefix)
            self._io.write_u1(self.num_out_path)
            for i in range(len(self.out_path)):
                pass
                self._io.write_u1(self.out_path[i])

            self._io.write_u1(self.num_in_path)
            for i in range(len(self.in_path)):
                pass
                self._io.write_u1(self.in_path[i])



        def _check(self):
            if len(self.pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"pub_key_prefix", 6, len(self.pub_key_prefix))
            if len(self.out_path) != self.num_out_path:
                raise kaitaistruct.ConsistencyError(u"out_path", self.num_out_path, len(self.out_path))
            for i in range(len(self.out_path)):
                pass

            if len(self.in_path) != self.num_in_path:
                raise kaitaistruct.ConsistencyError(u"in_path", self.num_in_path, len(self.in_path))
            for i in range(len(self.in_path)):
                pass

            self._dirty = False


    class PrivateKey(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.PrivateKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.private_key = self._io.read_bytes(64)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.PrivateKey, self)._write__seq(io)
            self._io.write_bytes(self.private_key)


        def _check(self):
            if len(self.private_key) != 64:
                raise kaitaistruct.ConsistencyError(u"private_key", 64, len(self.private_key))
            self._dirty = False


    class PubKeyPayload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.PubKeyPayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.PubKeyPayload, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class RawData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.RawData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.snr_raw = self._io.read_s4le()
            self.rssi = self._io.read_s4le()
            self.reserved = self._io.read_u1()
            self.payload = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.RawData, self)._write__seq(io)
            self._io.write_s4le(self.snr_raw)
            self._io.write_s4le(self.rssi)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.payload)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"payload", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False

        @property
        def snr(self):
            if hasattr(self, '_m_snr'):
                return self._m_snr

            self._m_snr = self.snr_raw / 4.0
            return getattr(self, '_m_snr', None)

        def _invalidate_snr(self):
            del self._m_snr

    class SelfInfo(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.SelfInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.advert_type = self._io.read_u1()
            self.tx_power_dbm = self._io.read_u1()
            self.max_tx_power_dbm = self._io.read_u1()
            self.public_key = self._io.read_bytes(32)
            self.latitude_microdegrees = self._io.read_u4le()
            self.longitude_microdegrees = self._io.read_u4le()
            self.multi_acks = self._io.read_u1()
            self.advert_loc_policy = KaitaiStream.resolve_enum(companion_common.CompanionCommon.AdvertLocPolicy, self._io.read_u1())
            self.telemetry_mode_base = self._io.read_bits_int_le(2)
            self.telemetry_mode_loc = self._io.read_bits_int_le(2)
            self.telemetry_mode_env = self._io.read_bits_int_le(2)
            self.unused = self._io.read_bits_int_le(2)
            self.manual_add_contacts = self._io.read_u1()
            self.raw_freq = self._io.read_u4le()
            self.raw_bw = self._io.read_u4le()
            self.sf = self._io.read_u1()
            self.cr = self._io.read_u1()
            self.node_name = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.SelfInfo, self)._write__seq(io)
            self._io.write_u1(self.advert_type)
            self._io.write_u1(self.tx_power_dbm)
            self._io.write_u1(self.max_tx_power_dbm)
            self._io.write_bytes(self.public_key)
            self._io.write_u4le(self.latitude_microdegrees)
            self._io.write_u4le(self.longitude_microdegrees)
            self._io.write_u1(self.multi_acks)
            self._io.write_u1(int(self.advert_loc_policy))
            self._io.write_bits_int_le(2, self.telemetry_mode_base)
            self._io.write_bits_int_le(2, self.telemetry_mode_loc)
            self._io.write_bits_int_le(2, self.telemetry_mode_env)
            self._io.write_bits_int_le(2, self.unused)
            self._io.write_u1(self.manual_add_contacts)
            self._io.write_u4le(self.raw_freq)
            self._io.write_u4le(self.raw_bw)
            self._io.write_u1(self.sf)
            self._io.write_u1(self.cr)
            self._io.write_bytes((self.node_name).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"node_name", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.public_key) != 32:
                raise kaitaistruct.ConsistencyError(u"public_key", 32, len(self.public_key))
            self._dirty = False

        @property
        def bw(self):
            if hasattr(self, '_m_bw'):
                return self._m_bw

            self._m_bw = self.raw_bw / 1000.0
            return getattr(self, '_m_bw', None)

        def _invalidate_bw(self):
            del self._m_bw
        @property
        def freq(self):
            if hasattr(self, '_m_freq'):
                return self._m_freq

            self._m_freq = self.raw_freq / 1000.0
            return getattr(self, '_m_freq', None)

        def _invalidate_freq(self):
            del self._m_freq
        @property
        def latitude(self):
            if hasattr(self, '_m_latitude'):
                return self._m_latitude

            self._m_latitude = self.latitude_microdegrees / 1000000.0
            return getattr(self, '_m_latitude', None)

        def _invalidate_latitude(self):
            del self._m_latitude
        @property
        def longitude(self):
            if hasattr(self, '_m_longitude'):
                return self._m_longitude

            self._m_longitude = self.longitude_microdegrees / 1000000.0
            return getattr(self, '_m_longitude', None)

        def _invalidate_longitude(self):
            del self._m_longitude

    class SendConfirmed(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.SendConfirmed, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.ack_crc = self._io.read_bytes(4)
            self.trip_time = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.SendConfirmed, self)._write__seq(io)
            self._io.write_bytes(self.ack_crc)
            self._io.write_u4le(self.trip_time)


        def _check(self):
            if len(self.ack_crc) != 4:
                raise kaitaistruct.ConsistencyError(u"ack_crc", 4, len(self.ack_crc))
            self._dirty = False


    class SnrItem(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.SnrItem, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.snr_raw = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.SnrItem, self)._write__seq(io)
            self._io.write_u1(self.snr_raw)


        def _check(self):
            self._dirty = False

        @property
        def snr(self):
            if hasattr(self, '_m_snr'):
                return self._m_snr

            self._m_snr = self.snr_raw / 4.0
            return getattr(self, '_m_snr', None)

        def _invalidate_snr(self):
            del self._m_snr

    class StatusResponse(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.StatusResponse, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.pub_key_prefix = self._io.read_bytes(6)
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.StatusResponse, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.pub_key_prefix)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"pub_key_prefix", 6, len(self.pub_key_prefix))
            self._dirty = False


    class TelemetryResponse(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.TelemetryResponse, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.pub_key_prefix = self._io.read_bytes(6)
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Companion.TelemetryResponse, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.pub_key_prefix)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"pub_key_prefix", 6, len(self.pub_key_prefix))
            self._dirty = False


    class TraceData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Companion.TraceData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.num_path = self._io.read_u1()
            self.flags = self._io.read_u1()
            self.tag = self._io.read_u4le()
            self.auth_code = self._io.read_u4le()
            self.path_hashes = []
            for i in range(self.num_path):
                self.path_hashes.append(self._io.read_u1())

            self.path_snrs_raw = []
            for i in range(self.num_path):
                _t_path_snrs_raw = Companion.SnrItem(self._io, self, self._root)
                try:
                    _t_path_snrs_raw._read()
                finally:
                    self.path_snrs_raw.append(_t_path_snrs_raw)

            self.final_snr_raw = self._io.read_s1()
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.path_hashes)):
                pass

            for i in range(len(self.path_snrs_raw)):
                pass
                self.path_snrs_raw[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Companion.TraceData, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_u1(self.num_path)
            self._io.write_u1(self.flags)
            self._io.write_u4le(self.tag)
            self._io.write_u4le(self.auth_code)
            for i in range(len(self.path_hashes)):
                pass
                self._io.write_u1(self.path_hashes[i])

            for i in range(len(self.path_snrs_raw)):
                pass
                self.path_snrs_raw[i]._write__seq(self._io)

            self._io.write_s1(self.final_snr_raw)


        def _check(self):
            if len(self.path_hashes) != self.num_path:
                raise kaitaistruct.ConsistencyError(u"path_hashes", self.num_path, len(self.path_hashes))
            for i in range(len(self.path_hashes)):
                pass

            if len(self.path_snrs_raw) != self.num_path:
                raise kaitaistruct.ConsistencyError(u"path_snrs_raw", self.num_path, len(self.path_snrs_raw))
            for i in range(len(self.path_snrs_raw)):
                pass
                if self.path_snrs_raw[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"path_snrs_raw", self._root, self.path_snrs_raw[i]._root)
                if self.path_snrs_raw[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"path_snrs_raw", self, self.path_snrs_raw[i]._parent)

            self._dirty = False

        @property
        def final_snr(self):
            if hasattr(self, '_m_final_snr'):
                return self._m_final_snr

            self._m_final_snr = self.final_snr_raw / 4.0
            return getattr(self, '_m_final_snr', None)

        def _invalidate_final_snr(self):
            del self._m_final_snr


