# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Meshcore(ReadWriteKaitaiStruct):

    class NodeType(IntEnum):
        none = 0
        chat = 1
        repeater = 2
        room_server = 3
        sensor = 4

    class PayloadType(IntEnum):
        req = 0
        response = 1
        txt_msg = 2
        ack = 3
        advert = 4
        grp_txt = 5
        grp_data = 6
        anon_req = 7
        path = 8
        trace = 9
        multipart = 10
        raw_custom = 15

    class RouteType(IntEnum):
        transport_flood = 0
        flood = 1
        direct = 2
        transport_direct = 3
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Meshcore, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.header = Meshcore.Header(self._io, self, self._root)
        self.header._read()
        if  ((self.header.route_type == Meshcore.RouteType.transport_flood) or (self.header.route_type == Meshcore.RouteType.transport_direct)) :
            pass
            self.transport_codes = Meshcore.TransportCodes(self._io, self, self._root)
            self.transport_codes._read()

        self.path = Meshcore.Path(self._io, self, self._root)
        self.path._read()
        _on = self.header.payload_type
        if _on == Meshcore.PayloadType.ack:
            pass
            self.payload = Meshcore.PayloadAck(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.advert:
            pass
            self.payload = Meshcore.PayloadAdvert(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.anon_req:
            pass
            self.payload = Meshcore.AnonReq(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.grp_data:
            pass
            self.payload = Meshcore.GrpData(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.grp_txt:
            pass
            self.payload = Meshcore.GrpData(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.multipart:
            pass
            self.payload = Meshcore.Multipart(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.path:
            pass
            self.payload = Meshcore.PayloadEncDirected(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.raw_custom:
            pass
            self.payload = Meshcore.RawCustom(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.req:
            pass
            self.payload = Meshcore.PayloadEncDirected(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.response:
            pass
            self.payload = Meshcore.PayloadEncDirected(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.trace:
            pass
            self.payload = Meshcore.Trace(self._io, self, self._root)
            self.payload._read()
        elif _on == Meshcore.PayloadType.txt_msg:
            pass
            self.payload = Meshcore.PayloadEncDirected(self._io, self, self._root)
            self.payload._read()
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        if  ((self.header.route_type == Meshcore.RouteType.transport_flood) or (self.header.route_type == Meshcore.RouteType.transport_direct)) :
            pass
            self.transport_codes._fetch_instances()

        self.path._fetch_instances()
        _on = self.header.payload_type
        if _on == Meshcore.PayloadType.ack:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.advert:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.anon_req:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.grp_data:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.grp_txt:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.multipart:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.path:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.raw_custom:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.req:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.response:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.trace:
            pass
            self.payload._fetch_instances()
        elif _on == Meshcore.PayloadType.txt_msg:
            pass
            self.payload._fetch_instances()


    def _write__seq(self, io=None):
        super(Meshcore, self)._write__seq(io)
        self.header._write__seq(self._io)
        if  ((self.header.route_type == Meshcore.RouteType.transport_flood) or (self.header.route_type == Meshcore.RouteType.transport_direct)) :
            pass
            self.transport_codes._write__seq(self._io)

        self.path._write__seq(self._io)
        _on = self.header.payload_type
        if _on == Meshcore.PayloadType.ack:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.advert:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.anon_req:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.grp_data:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.grp_txt:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.multipart:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.path:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.raw_custom:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.req:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.response:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.trace:
            pass
            self.payload._write__seq(self._io)
        elif _on == Meshcore.PayloadType.txt_msg:
            pass
            self.payload._write__seq(self._io)


    def _check(self):
        if self.header._root != self._root:
            raise kaitaistruct.ConsistencyError(u"header", self._root, self.header._root)
        if self.header._parent != self:
            raise kaitaistruct.ConsistencyError(u"header", self, self.header._parent)
        if  ((self.header.route_type == Meshcore.RouteType.transport_flood) or (self.header.route_type == Meshcore.RouteType.transport_direct)) :
            pass
            if self.transport_codes._root != self._root:
                raise kaitaistruct.ConsistencyError(u"transport_codes", self._root, self.transport_codes._root)
            if self.transport_codes._parent != self:
                raise kaitaistruct.ConsistencyError(u"transport_codes", self, self.transport_codes._parent)

        if self.path._root != self._root:
            raise kaitaistruct.ConsistencyError(u"path", self._root, self.path._root)
        if self.path._parent != self:
            raise kaitaistruct.ConsistencyError(u"path", self, self.path._parent)
        _on = self.header.payload_type
        if _on == Meshcore.PayloadType.ack:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.advert:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.anon_req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.grp_data:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.grp_txt:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.multipart:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.path:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.raw_custom:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.req:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.response:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.trace:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        elif _on == Meshcore.PayloadType.txt_msg:
            pass
            if self.payload._root != self._root:
                raise kaitaistruct.ConsistencyError(u"payload", self._root, self.payload._root)
            if self.payload._parent != self:
                raise kaitaistruct.ConsistencyError(u"payload", self, self.payload._parent)
        self._dirty = False

    class AdvertAppdata(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.AdvertAppdata, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.header = Meshcore.AdvertAppdataHeader(self._io, self, self._root)
            self.header._read()
            if self.header.has_location:
                pass
                self.latitude_microdegrees = self._io.read_s4le()

            if self.header.has_location:
                pass
                self.longitude_microdegrees = self._io.read_s4le()

            if self.header.has_feat1:
                pass
                self.feat1 = self._io.read_u2le()

            if self.header.has_feat2:
                pass
                self.feat2 = self._io.read_u2le()

            self.name = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            if self.header.has_location:
                pass

            if self.header.has_location:
                pass

            if self.header.has_feat1:
                pass

            if self.header.has_feat2:
                pass



        def _write__seq(self, io=None):
            super(Meshcore.AdvertAppdata, self)._write__seq(io)
            self.header._write__seq(self._io)
            if self.header.has_location:
                pass
                self._io.write_s4le(self.latitude_microdegrees)

            if self.header.has_location:
                pass
                self._io.write_s4le(self.longitude_microdegrees)

            if self.header.has_feat1:
                pass
                self._io.write_u2le(self.feat1)

            if self.header.has_feat2:
                pass
                self._io.write_u2le(self.feat2)

            self._io.write_bytes(self.name)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"name", 0, self._io.size() - self._io.pos())


        def _check(self):
            if self.header._root != self._root:
                raise kaitaistruct.ConsistencyError(u"header", self._root, self.header._root)
            if self.header._parent != self:
                raise kaitaistruct.ConsistencyError(u"header", self, self.header._parent)
            if self.header.has_location:
                pass

            if self.header.has_location:
                pass

            if self.header.has_feat1:
                pass

            if self.header.has_feat2:
                pass

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

    class AdvertAppdataHeader(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.AdvertAppdataHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.node_type = KaitaiStream.resolve_enum(Meshcore.NodeType, self._io.read_bits_int_le(4))
            self.has_location = self._io.read_bits_int_le(1) != 0
            self.has_feat1 = self._io.read_bits_int_le(1) != 0
            self.has_feat2 = self._io.read_bits_int_le(1) != 0
            self.has_name = self._io.read_bits_int_le(1) != 0
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.AdvertAppdataHeader, self)._write__seq(io)
            self._io.write_bits_int_le(4, int(self.node_type))
            self._io.write_bits_int_le(1, int(self.has_location))
            self._io.write_bits_int_le(1, int(self.has_feat1))
            self._io.write_bits_int_le(1, int(self.has_feat2))
            self._io.write_bits_int_le(1, int(self.has_name))


        def _check(self):
            self._dirty = False


    class AdvertSignData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.AdvertSignData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.public_key = self._io.read_bytes(32)
            self.timestamp = self._io.read_u4le()
            if (not (self._io.is_eof())):
                pass
                self.appdata = Meshcore.AdvertAppdata(self._io, self, self._root)
                self.appdata._read()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass
                self.appdata._fetch_instances()



        def _write__seq(self, io=None):
            super(Meshcore.AdvertSignData, self)._write__seq(io)
            self._io.write_bytes(self.public_key)
            self._io.write_u4le(self.timestamp)
            if (not (self._io.is_eof())):
                pass
                if self.appdata._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"appdata", self._root, self.appdata._root)
                if self.appdata._parent != self:
                    raise kaitaistruct.ConsistencyError(u"appdata", self, self.appdata._parent)
                self.appdata._write__seq(self._io)



        def _check(self):
            if len(self.public_key) != 32:
                raise kaitaistruct.ConsistencyError(u"public_key", 32, len(self.public_key))
            self._dirty = False


    class AnonReq(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.AnonReq, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.dst_hash = self._io.read_u1()
            self.public_key = self._io.read_bytes(32)
            self.cipher_mac = self._io.read_u2le()
            self.ciphertext = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.AnonReq, self)._write__seq(io)
            self._io.write_u1(self.dst_hash)
            self._io.write_bytes(self.public_key)
            self._io.write_u2le(self.cipher_mac)
            self._io.write_bytes(self.ciphertext)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"ciphertext", 0, self._io.size() - self._io.pos())


        def _check(self):
            if len(self.public_key) != 32:
                raise kaitaistruct.ConsistencyError(u"public_key", 32, len(self.public_key))
            self._dirty = False


    class GrpData(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.GrpData, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.channel_hash = self._io.read_u1()
            self.cipher_mac = self._io.read_u2le()
            self.ciphertext = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.GrpData, self)._write__seq(io)
            self._io.write_u1(self.channel_hash)
            self._io.write_u2le(self.cipher_mac)
            self._io.write_bytes(self.ciphertext)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"ciphertext", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Header(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.route_type = KaitaiStream.resolve_enum(Meshcore.RouteType, self._io.read_bits_int_le(2))
            self.payload_type = KaitaiStream.resolve_enum(Meshcore.PayloadType, self._io.read_bits_int_le(4))
            self.payload_version = self._io.read_bits_int_le(2)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.Header, self)._write__seq(io)
            self._io.write_bits_int_le(2, int(self.route_type))
            self._io.write_bits_int_le(4, int(self.payload_type))
            self._io.write_bits_int_le(2, self.payload_version)


        def _check(self):
            self._dirty = False


    class Multipart(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.Multipart, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.remaining = self._io.read_bits_int_le(4)
            self.payload_type = KaitaiStream.resolve_enum(Meshcore.PayloadType, self._io.read_bits_int_le(4))
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.Multipart, self)._write__seq(io)
            self._io.write_bits_int_le(4, self.remaining)
            self._io.write_bits_int_le(4, int(self.payload_type))
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Path(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.Path, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.num_nodes = self._io.read_u1()
            self.nodes = []
            for i in range(self.num_nodes):
                self.nodes.append(self._io.read_u1())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.nodes)):
                pass



        def _write__seq(self, io=None):
            super(Meshcore.Path, self)._write__seq(io)
            self._io.write_u1(self.num_nodes)
            for i in range(len(self.nodes)):
                pass
                self._io.write_u1(self.nodes[i])



        def _check(self):
            if len(self.nodes) != self.num_nodes:
                raise kaitaistruct.ConsistencyError(u"nodes", self.num_nodes, len(self.nodes))
            for i in range(len(self.nodes)):
                pass

            self._dirty = False


    class PayloadAck(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.PayloadAck, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.checksum = self._io.read_u4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.PayloadAck, self)._write__seq(io)
            self._io.write_u4le(self.checksum)


        def _check(self):
            self._dirty = False


    class PayloadAdvert(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.PayloadAdvert, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.public_key = self._io.read_bytes(32)
            self.timestamp = self._io.read_u4le()
            self.signature = self._io.read_bytes(64)
            if (not (self._io.is_eof())):
                pass
                self.appdata = Meshcore.AdvertAppdata(self._io, self, self._root)
                self.appdata._read()

            self._dirty = False


        def _fetch_instances(self):
            pass
            if (not (self._io.is_eof())):
                pass
                self.appdata._fetch_instances()



        def _write__seq(self, io=None):
            super(Meshcore.PayloadAdvert, self)._write__seq(io)
            self._io.write_bytes(self.public_key)
            self._io.write_u4le(self.timestamp)
            self._io.write_bytes(self.signature)
            if (not (self._io.is_eof())):
                pass
                if self.appdata._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"appdata", self._root, self.appdata._root)
                if self.appdata._parent != self:
                    raise kaitaistruct.ConsistencyError(u"appdata", self, self.appdata._parent)
                self.appdata._write__seq(self._io)



        def _check(self):
            if len(self.public_key) != 32:
                raise kaitaistruct.ConsistencyError(u"public_key", 32, len(self.public_key))
            if len(self.signature) != 64:
                raise kaitaistruct.ConsistencyError(u"signature", 64, len(self.signature))
            self._dirty = False


    class PayloadEncDirected(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.PayloadEncDirected, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.dst_hash = self._io.read_u1()
            self.src_hash = self._io.read_u1()
            self.cipher_mac = self._io.read_u2le()
            self.ciphertext = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.PayloadEncDirected, self)._write__seq(io)
            self._io.write_u1(self.dst_hash)
            self._io.write_u1(self.src_hash)
            self._io.write_u2le(self.cipher_mac)
            self._io.write_bytes(self.ciphertext)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"ciphertext", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class RawCustom(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.RawCustom, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.data = self._io.read_bytes_full()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.RawCustom, self)._write__seq(io)
            self._io.write_bytes(self.data)
            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"data", 0, self._io.size() - self._io.pos())


        def _check(self):
            self._dirty = False


    class Trace(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.Trace, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.trace_tag = self._io.read_u4le()
            self.auth_code = self._io.read_u4le()
            self.flags = self._io.read_u1()
            self.path = []
            i = 0
            while not self._io.is_eof():
                self.path.append(self._io.read_u1())
                i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.path)):
                pass



        def _write__seq(self, io=None):
            super(Meshcore.Trace, self)._write__seq(io)
            self._io.write_u4le(self.trace_tag)
            self._io.write_u4le(self.auth_code)
            self._io.write_u1(self.flags)
            for i in range(len(self.path)):
                pass
                if self._io.is_eof():
                    raise kaitaistruct.ConsistencyError(u"path", 0, self._io.size() - self._io.pos())
                self._io.write_u1(self.path[i])

            if not self._io.is_eof():
                raise kaitaistruct.ConsistencyError(u"path", 0, self._io.size() - self._io.pos())


        def _check(self):
            for i in range(len(self.path)):
                pass

            self._dirty = False


    class TransportCodes(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Meshcore.TransportCodes, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.val1 = self._io.read_u2le()
            self.val2 = self._io.read_u2le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Meshcore.TransportCodes, self)._write__seq(io)
            self._io.write_u2le(self.val1)
            self._io.write_u2le(self.val2)


        def _check(self):
            self._dirty = False



