from src.utils.arg_parser import parse_args
from src.utils.loader import read_from_file
from src.utils.validators import validate_url, validate_count
from src.utils.server_status_checker import run_check
from src.utils.output import write_output

def prepare_hosts(args) -> list[str]:
    """
    Получение списка хостов из аргументов
    """
    if args.hosts:
        hosts = [host.strip() for host in args.hosts.split(",")]
    else:
        hosts = read_from_file(args.file)

    valid_hosts = []

    for host in hosts:
        if validate_url(host):
            valid_hosts.append(host)
        else:
            print(f"Хост пропущен из-за ошибки валидации: {host}")

    if not valid_hosts:
        raise SystemExit("Нет валидных хостов для проверки")

    return valid_hosts


def main():
    """
    Комбинирование всех компонентов
    """
    args = parse_args()

    # Валидация count
    count = validate_count(args.count)

    # Получение списка хостов
    valid_hosts = prepare_hosts(args)

    # Проверка каждого хоста
    results = run_check(valid_hosts, count)

    write_output(results, args.output)