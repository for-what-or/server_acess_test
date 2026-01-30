import requests
from typing import List
import time
from typing import Dict

def format_results(results_list: List[dict]) -> str:
    """
    Форматирование результатов в читаемый вид.
    """
    lines = []
    for res in results_list:
        lines.append(f"Host: {res['host']}")
        lines.append(f"  Success: {res['success']}")
        lines.append(f"  Failed: {res['failed']}")
        lines.append(f"  Errors: {res['errors']}")
        if res['min'] is not None:
            lines.append(f"  Min: {res['min']:.3f} s")
            lines.append(f"  Max: {res['max']:.3f} s")
            lines.append(f"  Avg: {res['avg']:.3f} s")
        else:
            lines.append("  Min/Max/Avg: нет успешных запросов")
        lines.append("-" * 50)
    return "\n".join(lines)

def check_server_status(host: str, count: int = 1, timeout: int = 5) -> dict:
    """
    Проверка одного хоста. Возвращает статистику.
    """
    results = {
        "host": host,
        "success": 0,
        "failed": 0,
        "errors": 0,
        "times": []
    }

    for i in range(count):
        try:
            start = time.time()
            response = requests.get(host, timeout=timeout)
            elapsed = time.time() - start
            results["times"].append(elapsed)

            if response.status_code < 400:
                results["success"] += 1
            else:
                results["failed"] += 1

        except requests.RequestException:
            results["errors"] += 1

    # Статистика времени
    if results["times"]:
        results["min"] = min(results["times"])
        results["max"] = max(results["times"])
        results["avg"] = sum(results["times"]) / len(results["times"])
    else:
        results["min"] = results["max"] = results["avg"] = None

    return results


def check_servers(hosts: List[str], count: int = 1) -> List[Dict]:
    """
    Проверяем список серверов и результат выводим в виде словаря.
    """
    results = []

    for host in hosts:
        result = check_server_status(host, count)
        results.append(result)
        
    return results

def run_check(hosts: List[str], count: int = 1) -> str:
    """
    Комбинирование предыдущих компонентов.
    """
    result = check_servers(hosts, count)
    return format_results(result)