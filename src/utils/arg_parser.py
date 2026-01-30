import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Тестирование доступности серверов"
    )

    source_group = parser.add_mutually_exclusive_group(required=True)

    source_group.add_argument(
        "-H", "--hosts",
        type=str,
        help="Список HTTPS хостов, разделенных запятыми"
    )

    source_group.add_argument(
        "-F", "--file",
        type=str,
        help="Путь к файлу с HTTPS хостами (один хост на строку)"
    )

    parser.add_argument(
        "-C", "--count",
        default=1,
        type=str,
        help="Количество запросов к каждому хосту (по умолчанию: 1)"
    )

    parser.add_argument(
        "-O", "--output",
        type=str,
        help="Путь к файлу вывода (необязательно)"
    )

    args = parser.parse_args()

    return args

#перевод на русский