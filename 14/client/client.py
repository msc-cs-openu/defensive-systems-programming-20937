import socket
import struct
from proto import Request, Response, Status


class Client:
    """Client for communicating with the backup server."""

    def __init__(self, user_id: bytes, server_addr: tuple[str, int]):
        self.user_id = user_id
        self.server_addr = server_addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        """Use socket as a context manager and connect to the server."""
        self.sock.__enter__()
        self.sock.connect(self.server_addr)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the socket when leaving context manager."""
        return self.sock.__exit__(exc_type, exc_val, exc_tb)

    def send(self, req: Request) -> Response:
        """Send a request to the server and receive the response."""
        self.sock.sendall(req.pack())
        return self.receive()

    def receive(self) -> Response:
        """Receive a response from the server."""
        # Step 1: Read the fixed header
        header_size = struct.calcsize(Response._header_fmt)
        header = self._recv_exact(header_size)

        version, status, name_len, size = struct.unpack(
            Response._header_fmt, header)

        # Step 2: Read filename
        filename_bytes = self._recv_exact(name_len)
        filename = filename_bytes.decode("ascii")

        # Step 3: Read payload
        payload = self._recv_exact(size) if size > 0 else b""

        return Response(version, Status(status), filename, payload)

    def _recv_exact(self, n: int) -> bytes:
        """Read exactly n bytes from the socket."""
        buf = bytearray()
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("Socket closed while receiving data")
            buf.extend(chunk)
        return bytes(buf)
