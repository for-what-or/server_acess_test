import re
import argparse

def validate_url(url):
    """
    Проверка валидности одного URL
    """
    try:
        if url is None:
            raise ValueError("URL не задан")
        if not url:
            raise ValueError("URL пуст")
        if not isinstance(url, str):
            raise TypeError("URL должен быть строкой")
    
        url_pattern = "^https?://[-a-zA-Z0-9@:%._\\+~#=]+\\.[a-zA-Z0-9]{1,6}\\/*[-a-zA-Z0-9()@:%_\\+.~#?&/=]*$"
        
        if not re.match(url_pattern, url):
            raise ValueError("URL не соответствует требуемому шаблону")
        
        return True
    except (ValueError, TypeError) as e:
        print(f"Ошибка валидации URL: {e}")
        return False

def validate_count(value: str) -> int:
    """
    Проверка аргумента --count
    """
    try:
        count = int(value)
        if count <= 0:
            raise ValueError
        return count
    except ValueError:
        raise argparse.ArgumentTypeError("Аргумент --count должен быть положительным целым числом")