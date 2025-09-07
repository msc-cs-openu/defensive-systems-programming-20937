from proto import Request, Response, Op, Status
from utils import generate_user_id, get_server_addr, get_backup_files
from client import Client


def main():
    user_id = generate_user_id()
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

        print(res.__repr__())

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

        print(res.__repr__())

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

        print(res.__repr__())

        # ============== List files ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.List,
            filename="",
            payload=b""
        ))

        print(res.__repr__())

        # ============== Retrieve first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Retrieve,
            filename=first_file,
            payload=b""
        ))

        print(res.__repr__())

        # ============== Delete first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Delete,
            filename=first_file,
            payload=b""
        ))
        print(res.__repr__())

        # ============== Retrieve first file ==============

        res = sock.send(Request(
            user_id=user_id,
            version=1,
            op=Op.Retrieve,
            filename=first_file,
            payload=b""
        ))

        print(res.__repr__())


if __name__ == "__main__":
    main()
