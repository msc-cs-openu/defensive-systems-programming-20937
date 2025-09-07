import socket
from proto import Request, Response, Status


class Client:
    """Client for communicating with the backup server.
    """

    def __init__(self, user_id: bytes, server_addr: tuple[str, int]):
        self.user_id = user_id
        self.server_addr = server_addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        """Use socket as a context manager. and connect to the server.
        """
        self.sock.__enter__()
        self.sock.connect(self.server_addr)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Use socket as a context manager.
        """
        return self.sock.__exit__(exc_type, exc_val, exc_tb)

    def send(self, req: Request) -> Response:
        """Send a request to the server and receive the response.
        """
        self.sock.sendall(req.pack())
        return self.receive()

    def receive(self) -> Response:
        """Receive a response from the server.
        """
        version = int.from_bytes(self.sock.recv(1), byteorder='little')
        status = Status(int.from_bytes(self.sock.recv(2), byteorder='little'))
        name_len = int.from_bytes(self.sock.recv(2), byteorder='little')
        file_name = self.sock.recv(name_len).decode('ascii')
        size = int.from_bytes(self.sock.recv(4), byteorder='little')
        payload = self.sock.recv(size) if size > 0 else b''
        return Response(version, status, file_name, payload)
