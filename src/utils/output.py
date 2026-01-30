from pathlib import Path

def write_output(text: str, output_path: str | None = None) -> None:
    """
    Запись результата в файл или в консоль.

    Если файл вывода не указан, вывод происходит в консоль.
    """

    try:
        if output_path:
            path = Path(output_path)

            # создаем родительские директории при необходимости
            if path.parent and not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)

            with path.open("w", encoding="utf-8") as file:
                file.write(text)

            print(f"Результат успешно записан в файл: {path}")

        else:
            print(text)

    except OSError as e:
        print(f"Ошибка вывода: не удается записать в файл: {e}")

