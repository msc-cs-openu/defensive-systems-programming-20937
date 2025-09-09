from dataclasses import dataclass, field
from enum import IntEnum
from typing import ClassVar
import struct


class Op(IntEnum):
    """Operation codes for requests (1 byte)."""
    Save = 1
    Retrieve = 2
    Delete = 3
    List = 4


class Status(IntEnum):
    """Status codes for responses (2 bytes)."""
    SuccessRetrieved = 210
    SuccessListed = 211
    SuccessBackup = 212
    ErrorNotFound = 1001
    ErrorNoFiles = 1002
    ErrorGeneral = 1003


@dataclass
class Request:
    """Represents a client request message."""
    user_id: int
    version: int
    op: Op
    filename: str
    payload: bytes = field(default_factory=bytes)

    # user_id (4B), version (1B), op (1B), name_len (2B) → little endian
    _header_fmt: ClassVar[str] = "<IBBH"
    _size_fmt: ClassVar[str] = "<I"  # payload size (4B)

    def pack(self) -> bytes:
        filename_bytes = self.filename.encode("ascii")
        header = struct.pack(
            self._header_fmt,
            self.user_id,
            self.version,
            int(self.op),
            len(filename_bytes),
        )
        size_field = struct.pack(self._size_fmt, len(self.payload))
        return header + filename_bytes + size_field + self.payload

    @classmethod
    def unpack(cls, data: bytes) -> "Request":
        header_size = struct.calcsize(cls._header_fmt)
        if len(data) < header_size:
            raise ValueError("Data too short for Request header")

        user_id, version, op_val, name_len = struct.unpack(
            cls._header_fmt, data[:header_size]
        )

        filename_start = header_size
        filename_end = filename_start + name_len
        if len(data) < filename_end + 4:
            raise ValueError("Data too short for filename and size field")

        filename = data[filename_start:filename_end].decode("ascii")

        size_offset = filename_end
        (size,) = struct.unpack(cls._size_fmt,
                                data[size_offset:size_offset + 4])

        payload_start = size_offset + 4
        payload_end = payload_start + size
        if len(data) < payload_end:
            raise ValueError("Data too short for payload")

        payload = data[payload_start:payload_end]

        return cls(user_id, version, Op(op_val), filename, payload)


@dataclass
class Response:
    """Represents a server response message."""
    version: int
    status: Status
    filename: str
    payload: bytes = field(default_factory=bytes)

    # version (1B), status (2B), name_len (2B) → little endian
    _header_fmt: ClassVar[str] = "<BHH"
    _size_fmt: ClassVar[str] = "<I"  # payload size (4B)

    def pack(self) -> bytes:
        filename_bytes = self.filename.encode("ascii")
        header = struct.pack(
            self._header_fmt,
            self.version,
            int(self.status),
            len(filename_bytes),
        )
        size_field = struct.pack(self._size_fmt, len(self.payload))
        return header + filename_bytes + size_field + self.payload

    @classmethod
    def unpack(cls, data: bytes) -> "Response":
        header_size = struct.calcsize(cls._header_fmt)
        if len(data) < header_size:
            raise ValueError("Data too short for Response header")

        version, status_val, name_len = struct.unpack(
            cls._header_fmt, data[:header_size]
        )

        filename_start = header_size
        filename_end = filename_start + name_len
        if len(data) < filename_end + 4:
            raise ValueError("Data too short for filename and size field")

        filename = data[filename_start:filename_end].decode("ascii")

        size_offset = filename_end
        (size,) = struct.unpack(cls._size_fmt,
                                data[size_offset:size_offset + 4])

        payload_start = size_offset + 4
        payload_end = payload_start + size
        if len(data) < payload_end:
            raise ValueError("Data too short for payload")

        payload = data[payload_start:payload_end]

        return cls(version, Status(status_val), filename, payload)
