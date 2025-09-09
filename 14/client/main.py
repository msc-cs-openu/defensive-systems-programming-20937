import sys
from proto import Request, Op
from utils import generate_user_id, get_server_addr, get_backup_files
from client import Client


def main():
    user_id = int(sys.argv[1]) if len(sys.argv) > 1 else generate_user_id()
    server_ip, server_port = get_server_addr()
    [first_file, second_file] = get_backup_files()

    with Client(user_id, (server_ip, server_port)) as sock:
        print(f"Connection: {user_id}@{server_ip}:{server_port}")

        # ============== List files ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.List,
            filename="",
            payload=b""
        ))

        print(repr(res))

        # ============== Save first file ==============

        with open(first_file, "rb") as f:
            payload = f.read()

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Save,
            filename=first_file,
            payload=payload
        ))

        print(repr(res))

        # ============== Save second file ==============

        with open(second_file, "rb") as f:
            payload = f.read()

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Save,
            filename=second_file,
            payload=payload
        ))

        print(repr(res))

        # ============== List files ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.List,
            filename="",
            payload=b""
        ))

        print(repr(res))

        # ============== Retrieve first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Retrieve,
            filename=first_file,
            payload=b""
        ))

        print(repr(res))

        # ============== Delete first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Delete,
            filename=first_file,
            payload=b""
        ))

        print(repr(res))

        # ============== Retrieve first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Retrieve,
            filename=first_file,
            payload=b""
        ))

        print(repr(res))


if __name__ == "__main__":
    main()
