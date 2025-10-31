# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
import companion_common
import meshcore
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class CompanionCmds(ReadWriteKaitaiStruct):

    class Command(IntEnum):
        app_start = 1
        send_txt_msg = 2
        send_channel_txt_msg = 3
        get_contacts = 4
        get_device_time = 5
        set_device_time = 6
        send_self_advert = 7
        set_advert_name = 8
        add_update_contact = 9
        sync_next_message = 10
        set_radio_params = 11
        set_radio_tx_power = 12
        reset_path = 13
        set_advert_latlon = 14
        remove_contact = 15
        share_contact = 16
        export_contact = 17
        import_contact = 18
        reboot = 19
        get_batt_and_storage = 20
        set_tuning_params = 21
        device_query = 22
        export_private_key = 23
        import_private_key = 24
        send_raw_data = 25
        send_login = 26
        send_status_req = 27
        has_connection = 28
        logout = 29
        get_contact_by_key = 30
        get_channel = 31
        set_channel = 32
        sign_start = 33
        sign_data = 34
        sign_finish = 35
        send_trace_path = 36
        set_device_pin = 37
        set_other_params = 38
        send_telemetry_req = 39
        get_custom_vars = 40
        set_custom_var = 41
        get_advert_path = 42
        get_tuning_params = 43
        send_binary_req = 50
        factory_reset = 51
        send_path_discovery_req = 52
    def __init__(self, _io=None, _parent=None, _root=None):
        super(CompanionCmds, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.command = KaitaiStream.resolve_enum(CompanionCmds.Command, self._io.read_u1())
        _on = self.command
        if _on == CompanionCmds.Command.add_update_contact:
            pass
            self.payload = CompanionCmds.AddUpdateContact(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.app_start:
            pass
            self.payload = CompanionCmds.AppStart(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.device_query:
            pass
            self.payload = CompanionCmds.DeviceQuery(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.export_contact:
            pass
            self.payload = CompanionCmds.ExportContact(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.factory_reset:
            pass
            self.payload = CompanionCmds.FactoryReset(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.get_advert_path:
            pass
            self.payload = CompanionCmds.GetAdvertPath(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.get_channel:
            pass
            self.payload = CompanionCmds.GetChannel(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.get_contact_by_key:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.get_contacts:
            pass
            self.payload = CompanionCmds.GetContacts(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.has_connection:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.import_contact:
            pass
            self.payload = CompanionCmds.ImportContact(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.import_private_key:
            pass
            self.payload = CompanionCmds.ImportPrivateKey(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.logout:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.reboot:
            pass
            self.payload = CompanionCmds.Reboot(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.remove_contact:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.reset_path:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_binary_req:
            pass
            self.payload = CompanionCmds.SendBinaryReq(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_channel_txt_msg:
            pass
            self.payload = CompanionCmds.SendChannelTxtMsg(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_login:
            pass
            self.payload = CompanionCmds.SendLogin(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_path_discovery_req:
            pass
            self.payload = CompanionCmds.SendPathDiscoveryReq(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_raw_data:
            pass
            self.payload = CompanionCmds.SendRawData(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_self_advert:
            pass
            self.payload = CompanionCmds.SendSelfAdvert(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_status_req:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_telemetry_req:
            pass
            self.payload = CompanionCmds.SendTelemetryReq(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_trace_path:
            pass
            self.payload = CompanionCmds.SendTracePath(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.send_txt_msg:
            pass
            self.payload = CompanionCmds.SendTxtMsg(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_advert_latlon:
            pass
            self.payload = CompanionCmds.SetAdvertLatlon(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_advert_name:
            pass
            self.payload = CompanionCmds.SetAdvertName(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_channel:
            pass
            self.payload = CompanionCmds.SetChannel(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_custom_var:
            pass
            self.payload = CompanionCmds.SetCustomVar(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_device_pin:
            pass
            self.payload = CompanionCmds.SetDevicePin(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_device_time:
            pass
            self.payload = CompanionCmds.SetDeviceTime(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_other_params:
            pass
            self.payload = CompanionCmds.SetOtherParams(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_radio_params:
            pass
            self.payload = CompanionCmds.SetRadioParams(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_radio_tx_power:
            pass
            self.payload = CompanionCmds.SetRadioTxPower(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.set_tuning_params:
            pass
            self.payload = CompanionCmds.SetTuningParams(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.share_contact:
            pass
            self.payload = CompanionCmds.PubKeyPayload(self._io, self, self._root)
            self.payload._read()
        elif _on == CompanionCmds.Command.sign_data:
            pass
            self.payload = CompanionCmds.SignData(self._io, self, self._root)
            self.payload._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        _on = self.command
        if _on == CompanionCmds.Command.add_update_contact:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.app_start:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.device_query:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.export_contact:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.factory_reset:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.get_advert_path:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.get_channel:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.get_contact_by_key:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.get_contacts:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.has_connection:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.import_contact:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.import_private_key:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.logout:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.reboot:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.remove_contact:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.reset_path:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_binary_req:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_channel_txt_msg:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_login:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_path_discovery_req:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_raw_data:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_self_advert:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_status_req:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_telemetry_req:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_trace_path:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.send_txt_msg:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_advert_latlon:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_advert_name:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_channel:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_custom_var:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_device_pin:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_device_time:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_other_params:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_radio_params:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_radio_tx_power:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.set_tuning_params:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.share_contact:
            pass
            self.payload._fetch_instances()
        elif _on == CompanionCmds.Command.sign_data:
            pass
            self.payload._fetch_instances()


    def _write__seq(self, io=None):
        super(CompanionCmds, self)._write__seq(io)
        self._io.write_u1(int(self.command))
        _on = self.command
        if _on == CompanionCmds.Command.add_update_contact:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.app_start:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.device_query:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.export_contact:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.factory_reset:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.get_advert_path:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.get_channel:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.get_contact_by_key:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.get_contacts:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.has_connection:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.import_contact:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.import_private_key:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.logout:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.reboot:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.remove_contact:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.reset_path:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_binary_req:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_channel_txt_msg:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_login:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_path_discovery_req:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_raw_data:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_self_advert:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_status_req:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_telemetry_req:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_trace_path:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.send_txt_msg:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_advert_latlon:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_advert_name:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_channel:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_custom_var:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_device_pin:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_device_time:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_other_params:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_radio_params:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_radio_tx_power:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.set_tuning_params:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.share_contact:
            pass
            self.payload._write__seq(self._io)
        elif _on == CompanionCmds.Command.sign_data:
            pass
            self.payload._write__seq(self._io)


    def _check(self):
        _on = self.command
        if _on == CompanionCmds.Command.add_update_contact:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.app_start:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.device_query:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.export_contact:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.factory_reset:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.get_advert_path:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.get_channel:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.get_contact_by_key:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.get_contacts:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.has_connection:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.import_contact:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.import_private_key:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.logout:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.reboot:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.remove_contact:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.reset_path:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_binary_req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_channel_txt_msg:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_login:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_path_discovery_req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_raw_data:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_self_advert:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_status_req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_telemetry_req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_trace_path:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.send_txt_msg:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_advert_latlon:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_advert_name:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_channel:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_custom_var:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_device_pin:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_device_time:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_other_params:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_radio_params:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_radio_tx_power:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.set_tuning_params:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.share_contact:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == CompanionCmds.Command.sign_data:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        self._dirty = False

    class AddUpdateContact(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.AddUpdateContact, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self.type = KaitaiStream.resolve_enum(meshcore.Meshcore.NodeType, self._io.read_u1())
            self.flags = companion_common.CompanionCommon.ContactFlags(self._io)
            self.flags._read()
            self.num_out_path = self._io.read_u1()
            self.out_path = []
            for i in range(64):
                self.out_path.append(self._io.read_u1())

            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self.last_advert_timestamp = self._io.read_u4le()
            if (not (self._io.is_eof())):
                pass
                self.location = CompanionCmds.AddUpdateContactLoc(self._io, self, self._root)
                self.location._read()

            if (not (self._io.is_eof())):
                pass
                self.lastmod = self._io.read_u4le()

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()
            for i in range(len(self.out_path)):
                pass

            if (not (self._io.is_eof())):
                pass
                self.location._fetch_instances()

            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.AddUpdateContact, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)
            self._io.write_u1(int(self.type))
            self.flags._write__seq(self._io)
            self._io.write_u1(self.num_out_path)
            for i in range(len(self.out_path)):
                pass
                self._io.write_u1(self.out_path[i])

            self._io.write_bytes_limit((self.name).encode(u"UTF-8"), 32, 0, 0)
            self._io.write_u4le(self.last_advert_timestamp)
            if (not (self._io.is_eof())):
                pass
                if self.location._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"location", self._root, self.location._root)
                if self.location._parent != self:
                    raise kaitaistruct.ConsistencyError(u"location", self, self.location._parent)
                self.location._write__seq(self._io)

            if (not (self._io.is_eof())):
                pass
                self._io.write_u4le(self.lastmod)



        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            if len(self.out_path) != 64:
                raise kaitaistruct.ConsistencyError(u"out_path", 64, len(self.out_path))
            for i in range(len(self.out_path)):
                pass

            if len((self.name).encode(u"UTF-8")) > 32:
                raise kaitaistruct.ConsistencyError(u"name", 32, len((self.name).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"name", -1, KaitaiStream.byte_array_index_of((self.name).encode(u"UTF-8"), 0))
            self._dirty = False


    class AddUpdateContactLoc(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.AddUpdateContactLoc, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.latitude_microdegrees = self._io.read_u4le()
            self.longitude_microdegrees = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.AddUpdateContactLoc, self)._write__seq(io)
            self._io.write_u4le(self.latitude_microdegrees)
            self._io.write_u4le(self.longitude_microdegrees)


        def _check(self):
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

    class AppStart(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.AppStart, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_bytes(7)
            self.app_name = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.AppStart, self)._write__seq(io)
            self._io.write_bytes(self.reserved)
            self._io.write_bytes((self.app_name).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"app_name", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.reserved) != 7:
                raise kaitaistruct.ConsistencyError(u"reserved", 7, len(self.reserved))
            self._dirty = False


    class DeviceQuery(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.DeviceQuery, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.app_target_ver = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.DeviceQuery, self)._write__seq(io)
            self._io.write_u1(self.app_target_ver)


        def _check(self):
            self._dirty = False


    class ExportContact(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.ExportContact, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if (not (self._io.is_eof())):
                pass
                self.pub_key = self._io.read_bytes(32)

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.ExportContact, self)._write__seq(io)
            if (not (self._io.is_eof())):
                pass
                if len(self.pub_key) != 32:
                    raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
                self._io.write_bytes(self.pub_key)



        def _check(self):
            self._dirty = False


    class FactoryReset(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.FactoryReset, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reset = self._io.read_bytes(5)
            if not self.reset == b"\x72\x65\x73\x65\x74":
                raise kaitaistruct.ValidationNotEqualError(b"\x72\x65\x73\x65\x74", self.reset, self._io, u"/types/factory_reset/seq/0")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.FactoryReset, self)._write__seq(io)
            self._io.write_bytes(self.reset)


        def _check(self):
            if len(self.reset) != 5:
                raise kaitaistruct.ConsistencyError(u"reset", 5, len(self.reset))
            if not self.reset == b"\x72\x65\x73\x65\x74":
                raise kaitaistruct.ValidationNotEqualError(b"\x72\x65\x73\x65\x74", self.reset, None, u"/types/factory_reset/seq/0")
            self._dirty = False


    class GetAdvertPath(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.GetAdvertPath, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            self.pub_key = self._io.read_bytes(32)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.GetAdvertPath, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.pub_key)


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class GetChannel(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.GetChannel, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.channel_idx = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.GetChannel, self)._write__seq(io)
            self._io.write_u1(self.channel_idx)


        def _check(self):
            self._dirty = False


    class GetContacts(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.GetContacts, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if (not (self._io.is_eof())):
                pass
                self.since = self._io.read_u4le()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.GetContacts, self)._write__seq(io)
            if (not (self._io.is_eof())):
                pass
                self._io.write_u4le(self.since)



        def _check(self):
            self._dirty = False


    class ImportContact(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.ImportContact, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.advert_packet = meshcore.Meshcore(self._io)
            self.advert_packet._read()
            _ = self.advert_packet
            if not _.header.payload_type == meshcore.Meshcore.PayloadType.advert:
                raise kaitaistruct.ValidationExprError(self.advert_packet, self._io, u"/types/import_contact/seq/0")
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.advert_packet._fetch_instances()


        def _write__seq(self, io=None):
            super(CompanionCmds.ImportContact, self)._write__seq(io)
            self.advert_packet._write__seq(self._io)


        def _check(self):
            _ = self.advert_packet
            if not _.header.payload_type == meshcore.Meshcore.PayloadType.advert:
                raise kaitaistruct.ValidationExprError(self.advert_packet, None, u"/types/import_contact/seq/0")
            self._dirty = False


    class ImportPrivateKey(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.ImportPrivateKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.private_key = self._io.read_bytes(64)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.ImportPrivateKey, self)._write__seq(io)
            self._io.write_bytes(self.private_key)


        def _check(self):
            if len(self.private_key) != 64:
                raise kaitaistruct.ConsistencyError(u"private_key", 64, len(self.private_key))
            self._dirty = False


    class PubKeyPayload(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.PubKeyPayload, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.PubKeyPayload, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class Reboot(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.Reboot, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reboot = self._io.read_bytes(6)
            if not self.reboot == b"\x72\x65\x62\x6F\x6F\x74":
                raise kaitaistruct.ValidationNotEqualError(b"\x72\x65\x62\x6F\x6F\x74", self.reboot, self._io, u"/types/reboot/seq/0")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.Reboot, self)._write__seq(io)
            self._io.write_bytes(self.reboot)


        def _check(self):
            if len(self.reboot) != 6:
                raise kaitaistruct.ConsistencyError(u"reboot", 6, len(self.reboot))
            if not self.reboot == b"\x72\x65\x62\x6F\x6F\x74":
                raise kaitaistruct.ValidationNotEqualError(b"\x72\x65\x62\x6F\x6F\x74", self.reboot, None, u"/types/reboot/seq/0")
            self._dirty = False


    class SendBinaryReq(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendBinaryReq, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self.req_data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendBinaryReq, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)
            self._io.write_bytes(self.req_data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"req_data", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class SendChannelTxtMsg(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendChannelTxtMsg, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.txt_type = KaitaiStream.resolve_enum(companion_common.CompanionCommon.TxtType, self._io.read_u1())
            if not self.txt_type == companion_common.CompanionCommon.TxtType.plain:
                raise kaitaistruct.ValidationNotEqualError(companion_common.CompanionCommon.TxtType.plain, self.txt_type, self._io, u"/types/send_channel_txt_msg/seq/0")
            self.channel_idx = self._io.read_u1()
            self.msg_timestamp = self._io.read_u4le()
            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendChannelTxtMsg, self)._write__seq(io)
            self._io.write_u1(int(self.txt_type))
            self._io.write_u1(self.channel_idx)
            self._io.write_u4le(self.msg_timestamp)
            self._io.write_bytes((self.text).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"text", 0, self._io.size() - self._io.pos())


        def _check(self):
            if not self.txt_type == companion_common.CompanionCommon.TxtType.plain:
                raise kaitaistruct.ValidationNotEqualError(companion_common.CompanionCommon.TxtType.plain, self.txt_type, None, u"/types/send_channel_txt_msg/seq/0")
            self._dirty = False


    class SendLogin(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendLogin, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pub_key = self._io.read_bytes(32)
            self.password = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendLogin, self)._write__seq(io)
            self._io.write_bytes(self.pub_key)
            self._io.write_bytes((self.password).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"password", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class SendPathDiscoveryReq(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendPathDiscoveryReq, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.reserved = self._io.read_u1()
            if not self.reserved == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved, self._io, u"/types/send_path_discovery_req/seq/0")
            self.pub_key = self._io.read_bytes(32)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendPathDiscoveryReq, self)._write__seq(io)
            self._io.write_u1(self.reserved)
            self._io.write_bytes(self.pub_key)


        def _check(self):
            if not self.reserved == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved, None, u"/types/send_path_discovery_req/seq/0")
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class SendRawData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendRawData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_path = self._io.read_u1()
            self.path = []
            for i in range(self.num_path):
                self.path.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.path)):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.SendRawData, self)._write__seq(io)
            self._io.write_u1(self.num_path)
            for i in range(len(self.path)):
                pass
                self._io.write_u1(self.path[i])



        def _check(self):
            if len(self.path) != self.num_path:
                raise kaitaistruct.ConsistencyError(u"path", self.num_path, len(self.path))
            for i in range(len(self.path)):
                pass

            self._dirty = False


    class SendSelfAdvert(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendSelfAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            if (not (self._io.is_eof())):
                pass
                self.flood = self._io.read_u1()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.SendSelfAdvert, self)._write__seq(io)
            if (not (self._io.is_eof())):
                pass
                self._io.write_u1(self.flood)



        def _check(self):
            self._dirty = False


    class SendTelemetryReq(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendTelemetryReq, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unused = self._io.read_bytes(3)
            self.pub_key = self._io.read_bytes(32)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendTelemetryReq, self)._write__seq(io)
            self._io.write_bytes(self.unused)
            self._io.write_bytes(self.pub_key)


        def _check(self):
            if len(self.unused) != 3:
                raise kaitaistruct.ConsistencyError(u"unused", 3, len(self.unused))
            if len(self.pub_key) != 32:
                raise kaitaistruct.ConsistencyError(u"pub_key", 32, len(self.pub_key))
            self._dirty = False


    class SendTracePath(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendTracePath, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.tag = self._io.read_u4le()
            self.auth = self._io.read_u4le()
            self.flags = self._io.read_u1()
            self.path = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendTracePath, self)._write__seq(io)
            self._io.write_u4le(self.tag)
            self._io.write_u4le(self.auth)
            self._io.write_u1(self.flags)
            self._io.write_bytes(self.path)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"path", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SendTxtMsg(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SendTxtMsg, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.txt_type = KaitaiStream.resolve_enum(companion_common.CompanionCommon.TxtType, self._io.read_u1())
            self.attempt = self._io.read_u1()
            self.msg_timestamp = self._io.read_u4le()
            self.pub_key_prefix = self._io.read_bytes(6)
            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SendTxtMsg, self)._write__seq(io)
            self._io.write_u1(int(self.txt_type))
            self._io.write_u1(self.attempt)
            self._io.write_u4le(self.msg_timestamp)
            self._io.write_bytes(self.pub_key_prefix)
            self._io.write_bytes((self.text).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"text", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.pub_key_prefix) != 6:
                raise kaitaistruct.ConsistencyError(u"pub_key_prefix", 6, len(self.pub_key_prefix))
            self._dirty = False


    class SetAdvertLatlon(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetAdvertLatlon, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.latitude_microdegrees = self._io.read_u4le()
            self.longitude_microdegrees = self._io.read_u4le()
            if (not (self._io.is_eof())):
                pass
                self.altitude = self._io.read_u4le()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.SetAdvertLatlon, self)._write__seq(io)
            self._io.write_u4le(self.latitude_microdegrees)
            self._io.write_u4le(self.longitude_microdegrees)
            if (not (self._io.is_eof())):
                pass
                self._io.write_u4le(self.altitude)



        def _check(self):
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

    class SetAdvertName(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetAdvertName, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetAdvertName, self)._write__seq(io)
            self._io.write_bytes((self.name).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"name", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SetChannel(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetChannel, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.channel_idx = self._io.read_u1()
            self.channel_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self.channel_secret = self._io.read_bytes(16)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetChannel, self)._write__seq(io)
            self._io.write_u1(self.channel_idx)
            self._io.write_bytes_limit((self.channel_name).encode(u"UTF-8"), 32, 0, 0)
            self._io.write_bytes(self.channel_secret)


        def _check(self):
            if len((self.channel_name).encode(u"UTF-8")) > 32:
                raise kaitaistruct.ConsistencyError(u"channel_name", 32, len((self.channel_name).encode(u"UTF-8")))
            if KaitaiStream.byte_array_index_of((self.channel_name).encode(u"UTF-8"), 0) != -1:
                raise kaitaistruct.ConsistencyError(u"channel_name", -1, KaitaiStream.byte_array_index_of((self.channel_name).encode(u"UTF-8"), 0))
            if len(self.channel_secret) != 16:
                raise kaitaistruct.ConsistencyError(u"channel_secret", 16, len(self.channel_secret))
            self._dirty = False


    class SetCustomVar(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetCustomVar, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetCustomVar, self)._write__seq(io)
            self._io.write_bytes((self.value).encode(u"UTF-8"))
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"value", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class SetDevicePin(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetDevicePin, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.pin = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetDevicePin, self)._write__seq(io)
            self._io.write_u4le(self.pin)


        def _check(self):
            self._dirty = False


    class SetDeviceTime(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetDeviceTime, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.secs = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetDeviceTime, self)._write__seq(io)
            self._io.write_u4le(self.secs)


        def _check(self):
            self._dirty = False


    class SetOtherParams(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetOtherParams, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.manual_add_contacts = self._io.read_u1()
            if (not (self._io.is_eof())):
                pass
                self.telemetry = CompanionCmds.SetOtherParamsTelemetry(self._io, self, self._root)
                self.telemetry._read()

            if (not (self._io.is_eof())):
                pass
                self.multi_acks = self._io.read_u1()

            if (not (self._io.is_eof())):
                pass
                self.advert_loc_policy = KaitaiStream.resolve_enum(companion_common.CompanionCommon.AdvertLocPolicy, self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass
                self.telemetry._fetch_instances()

            if (not (self._io.is_eof())):
                pass

            if (not (self._io.is_eof())):
                pass



        def _write__seq(self, io=None):
            super(CompanionCmds.SetOtherParams, self)._write__seq(io)
            self._io.write_u1(self.manual_add_contacts)
            if (not (self._io.is_eof())):
                pass
                if self.telemetry._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"telemetry", self._root, self.telemetry._root)
                if self.telemetry._parent != self:
                    raise kaitaistruct.ConsistencyError(u"telemetry", self, self.telemetry._parent)
                self.telemetry._write__seq(self._io)

            if (not (self._io.is_eof())):
                pass
                self._io.write_u1(self.multi_acks)

            if (not (self._io.is_eof())):
                pass
                self._io.write_u1(int(self.advert_loc_policy))



        def _check(self):
            self._dirty = False


    class SetOtherParamsTelemetry(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetOtherParamsTelemetry, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.telemetry_mode_base = self._io.read_bits_int_le(2)
            self.telemetry_mode_loc = self._io.read_bits_int_le(2)
            self.telemetry_mode_env = self._io.read_bits_int_le(2)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetOtherParamsTelemetry, self)._write__seq(io)
            self._io.write_bits_int_le(2, self.telemetry_mode_base)
            self._io.write_bits_int_le(2, self.telemetry_mode_loc)
            self._io.write_bits_int_le(2, self.telemetry_mode_env)


        def _check(self):
            self._dirty = False


    class SetRadioParams(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetRadioParams, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.freq_khz = self._io.read_u4le()
            self.bw_khz = self._io.read_u4le()
            self.sf = self._io.read_u1()
            self.cr = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetRadioParams, self)._write__seq(io)
            self._io.write_u4le(self.freq_khz)
            self._io.write_u4le(self.bw_khz)
            self._io.write_u1(self.sf)
            self._io.write_u1(self.cr)


        def _check(self):
            self._dirty = False

        @property
        def bw_mhz(self):
            if hasattr(self, '_m_bw_mhz'):
                return self._m_bw_mhz

            self._m_bw_mhz = self.bw_khz / 1000.0
            return getattr(self, '_m_bw_mhz', None)

        def _invalidate_bw_mhz(self):
            del self._m_bw_mhz
        @property
        def freq_mhz(self):
            if hasattr(self, '_m_freq_mhz'):
                return self._m_freq_mhz

            self._m_freq_mhz = self.freq_khz / 1000.0
            return getattr(self, '_m_freq_mhz', None)

        def _invalidate_freq_mhz(self):
            del self._m_freq_mhz

    class SetRadioTxPower(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetRadioTxPower, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.tx_power = self._io.read_u1()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetRadioTxPower, self)._write__seq(io)
            self._io.write_u1(self.tx_power)


        def _check(self):
            self._dirty = False


    class SetTuningParams(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SetTuningParams, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.rx = self._io.read_u4le()
            self.af = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SetTuningParams, self)._write__seq(io)
            self._io.write_u4le(self.rx)
            self._io.write_u4le(self.af)


        def _check(self):
            self._dirty = False


    class SignData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCmds.SignData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCmds.SignData, self)._write__seq(io)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False



