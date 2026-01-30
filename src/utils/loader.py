from pathlib import Path
import argparse

def read_from_file(path: str) -> list[str]:
    """
    Чтение хостов из файла (по одной строке на хост)
    """

    file_path = Path(path)

    if not file_path.exists():
        raise argparse.ArgumentTypeError(
            f"Файл с хостами не найден: {path}"
        )

    if not file_path.is_file():
        raise argparse.ArgumentTypeError(
            f"Путь не является файлом: {path}"
        )

    try:
        with file_path.open("r", encoding="utf-8") as file:
            hosts = [
                line.strip()
                for line in file
                if line.strip()
            ]
    except OSError as e:
        raise argparse.ArgumentTypeError(
            f"Ошибка при чтении файла с хостами: {e}"
        )

    if not hosts:
        raise argparse.ArgumentTypeError(
            "Файл с хостами пуст"
        )

    return hosts

