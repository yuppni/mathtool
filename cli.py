from argparse import *
from calc.series import FORMULAS
from calc.integration import FUNCTIONS
from calc.arrays import MIN_VALUE, MAX_VALUE
from calc.sorting import METHODS


def create_parser():
    """Создаёт и возвращает разборщик команд и параметров приложения."""
    # Общий разборщик командной строки
    parser = ArgumentParser(
        prog="mathtool",
        description="Решение уравнений, статистика, ряды и интегралы",
        allow_abbrev=False
    )
    commands = parser.add_subparsers(dest="command")

    # Решение уравнения: коэффициенты необязательны,
    # поскольку остаётся ввод с клавиатуры
    solve_parser = commands.add_parser(
        "solve", help="решение уравнения", allow_abbrev=False
    )
    solve_parser.add_argument("-a", type=int, help="коэффициент A")
    solve_parser.add_argument("-b", type=int, help="коэффициент B")
    solve_parser.add_argument("-c", type=int, help="коэффициент C")

    # Без --input числа будут читаться со стандартного ввода
    stats_parser = commands.add_parser(
        "stats", help="статистика", allow_abbrev=False
    )
    stats_parser.add_argument("--input", help="файл с числами")

    # Допустимые названия рядов берём из таблицы FORMULAS
    series_parser = commands.add_parser(
        "series", help="сумма ряда", allow_abbrev=False
    )
    series_parser.add_argument(
        "--func", required=True,
        choices=sorted(FORMULAS), help="название ряда"
    )

    # Пользователь должен указать ровно один способ остановки
    stop = series_parser.add_mutually_exclusive_group(required=True)
    stop.add_argument("--terms", type=int, help="количество слагаемых")
    stop.add_argument("--eps", type=float, help="точность")

    # Допустимые функции берём из таблицы FUNCTIONS
    integrate_parser = commands.add_parser(
        "integrate", help="интегрирование", allow_abbrev=False
    )
    integrate_parser.add_argument(
        "--func", required=True,
        choices=sorted(FUNCTIONS), help="название функции"
    )

    # dest задаёт имя, под которым получим значение после разбора
    integrate_parser.add_argument(
        "--from", dest="start", type=float,
        required=True, help="нижний предел"
    )
    integrate_parser.add_argument(
        "--to", dest="end", type=float,
        required=True, help="верхний предел"
    )
    integrate_parser.add_argument(
        "--steps", type=int, required=True,
        help="количество прямоугольников"
    )
    # Генерация массива
    fill_parser = commands.add_parser(
        "fill", help="генерация массива", allow_abbrev=False
    )
    fill_parser.add_argument(
        "-c", "--count", type=int, required=True,
        help="количество элементов"
    )
    fill_parser.add_argument(
        "--min", type=int, default=MIN_VALUE,
        help="нижняя граница значений"
    )
    fill_parser.add_argument(
        "--max", type=int, default=MAX_VALUE,
        help="верхняя граница значений"
    )
    fill_parser.add_argument(
        "--seed", type=int,
        help="начальное значение генератора"
    )
    fill_parser.add_argument(
        "-o", "--output",
        help="файл для созданного массива"
    )

    # Сортировка массива
    sort_parser = commands.add_parser(
        "sort", help="сортировка массива", allow_abbrev=False
    )
    sort_parser.add_argument(
        "-m", "--method", required=True,
        choices=sorted(METHODS),
        help="метод сортировки"
    )
    sort_parser.add_argument(
        "--order", choices=["asc", "desc"], default="asc",
        help="направление: asc — возрастание, desc — убывание"
    )
    sort_parser.add_argument(
        "-i", "--input",
        help="файл с исходным массивом"
    )
    sort_parser.add_argument(
        "-o", "--output",
        help="файл для отсортированного массива"
    )

    # Двоичный поиск
    search_parser = commands.add_parser(
        "search", help="поиск числа в массиве", allow_abbrev=False
    )
    search_parser.add_argument(
        "-v", "--value", type=int, required=True,
        help="искомое целое число"
    )
    search_parser.add_argument(
        "-i", "--input",
        help="файл с массивом по возрастанию"
    )
    # Возвращаем настроенный разборщик в mathtool.py
    return parser