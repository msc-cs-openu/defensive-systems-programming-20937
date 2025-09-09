import socket
import struct
from proto import Request, Response, Status


class Client:
    """Client for communicating with the backup server."""

    def __init__(self, user_id: int, server_addr: tuple[str, int]):
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
        data = req.pack()
        print(f"[DEBUG] Sending {len(data)} bytes")
        self.sock.sendall(data)
        return self.receive()

    def receive(self) -> Response:
        """Receive a response from the server."""
        # Step 1: Read header (version, status, name_len)
        header_size = struct.calcsize(Response._header_fmt)
        print(f"[DEBUG] Reading header {header_size} bytes")
        header = self._recv_exact(header_size)
        version, status_val, name_len = struct.unpack(
            Response._header_fmt, header)

        # Step 2: Read filename
        print(f"[DEBUG] Reading filename {name_len} bytes")
        filename_bytes = self._recv_exact(name_len)
        filename = filename_bytes.decode("ascii") if name_len > 0 else ""

        # Step 3: Read payload size (4 bytes)
        print("[DEBUG] Reading payload size (4 bytes)")
        size_data = self._recv_exact(struct.calcsize(Response._size_fmt))
        (size,) = struct.unpack(Response._size_fmt, size_data)

        # Step 4: Read payload
        print(f"[DEBUG] Reading payload {size} bytes")
        payload = self._recv_exact(size) if size > 0 else b""

        print(f"[DEBUG] Received Response(version={version},"
              f" status={status_val}, filename='{filename}',"
              f" payload_len={len(payload)})")
        return Response(version, Status(status_val), filename, payload)

    def _recv_exact(self, n: int) -> bytes:
        """Read exactly n bytes from the socket safely."""
        if n == 0:
            return b""
        buf = bytearray()
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError(
                    f"Socket closed while receiving {n} bytes, got {len(buf)} bytes"
                )
            buf.extend(chunk)
        return bytes(buf)
