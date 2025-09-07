from pathlib import Path
import os


def get_server_addr(file_path: Path | None = None) -> tuple[str, int]:
    """Get the server address from a file.
    """
    file_path = file_path or Path.cwd() / "server.info"

    assert file_path.exists(), \
        f"Server info file `{file_path}` does not exist."

    with file_path.open("r") as f:
        line = f.readline().strip()

    try:
        host, port_str = line.split(":")
        port = int(port_str)
        assert 0 <= port <= 65535, "Port number must be between 0 and 65535."
    except ValueError:
        raise ValueError("Server info file must contain 'host:port' format.")

    return host, port


def get_backup_files(file_path: Path | None = None) -> list[str]:
    """Get the list of backup files from a file.
    """
    file_path = file_path or Path.cwd() / "backup.info"

    assert file_path.exists(), \
        f"Backup info file `{file_path}` does not exist."

    with file_path.open("r") as f:
        lines = [line.strip() for line in f if line.strip()]

    return lines


def generate_user_id() -> int:
    """Generate a random 4-byte user ID.
    """
    return os.urandom(4)
