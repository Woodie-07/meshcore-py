# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class CompanionCommon(ReadWriteKaitaiStruct):

    class AdvertLocPolicy(IntEnum):
        none = 0
        share = 1

    class TxtType(IntEnum):
        plain = 0
        cli_data = 1
        signed_plain = 2
    def __init__(self, _io=None, _parent=None, _root=None):
        super(CompanionCommon, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        pass
        self._dirty = False


    def _fetch_instances(self):
        pass


    def _write__seq(self, io=None):
        super(CompanionCommon, self)._write__seq(io)


    def _check(self):
        self._dirty = False

    class ContactFlags(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(CompanionCommon.ContactFlags, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.favourite = self._io.read_bits_int_le(1) != 0
            self.telem_perm_base = self._io.read_bits_int_le(1) != 0
            self.telem_perm_location = self._io.read_bits_int_le(1) != 0
            self.telem_perm_environment = self._io.read_bits_int_le(1) != 0
            self.unused = self._io.read_bits_int_le(4)
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(CompanionCommon.ContactFlags, self)._write__seq(io)
            self._io.write_bits_int_le(1, int(self.favourite))
            self._io.write_bits_int_le(1, int(self.telem_perm_base))
            self._io.write_bits_int_le(1, int(self.telem_perm_location))
            self._io.write_bits_int_le(1, int(self.telem_perm_environment))
            self._io.write_bits_int_le(4, self.unused)


        def _check(self):
            self._dirty = False



