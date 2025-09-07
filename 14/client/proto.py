from dataclasses import dataclass, field
from enum import IntEnum
from typing import ClassVar
import struct


class Op(IntEnum):
    """Operation codes for requests.
    """
    Save = 100
    Retrieve = 200
    Delete = 201
    List = 202


class Status(IntEnum):
    """Status codes for responses.
    """
    SuccessRetrieved = 210
    SuccessListed = 211
    SuccessBackup = 212
    ErrorNotFound = 1001
    ErrorNoFiles = 1002
    ErrorGeneral = 1003


@dataclass
class Request:
    """Represents a client request message.
    """
    user_id: int
    version: int
    op: Op
    filename: str
    payload: bytes = field(default_factory=bytes)

    _header_fmt: ClassVar[str] = "<IBBH I"

    def pack(self) -> bytes:
        filename_bytes = self.filename.encode("ascii")
        header = struct.pack(
            self._header_fmt,
            self.user_id,
            self.version,
            self.op,
            len(filename_bytes),
            len(self.payload)
        )
        return header + filename_bytes + self.payload

    @classmethod
    def unpack(cls, data: bytes) -> "Request":
        header_size = struct.calcsize(cls._header_fmt)
        user_id, version, op, name_len, size = struct.unpack(
            cls._header_fmt, data[:header_size])
        filename = data[header_size:header_size + name_len].decode("ascii")
        payload = data[header_size + name_len:header_size + name_len + size]
        return cls(user_id, version, Op(op), filename, payload)


@dataclass
class Response:
    """Represents a server response message.
    """
    version: int
    status: Status
    filename: str
    payload: bytes = field(default_factory=bytes)

    _header_fmt: ClassVar[str] = "<B H H I"

    def pack(self) -> bytes:
        filename_bytes = self.filename.encode("ascii")
        header = struct.pack(
            self._header_fmt,
            self.version,
            self.status,
            len(filename_bytes),
            len(self.payload)
        )
        return header + filename_bytes + self.payload

    @classmethod
    def unpack(cls, data: bytes) -> "Response":
        header_size = struct.calcsize(cls._header_fmt)
        version, status, name_len, size = struct.unpack(
            cls._header_fmt, data[:header_size])
        filename = data[header_size:header_size + name_len].decode("ascii")
        payload = data[header_size + name_len:header_size + name_len + size]
        return cls(version, Status(status), filename, payload)
