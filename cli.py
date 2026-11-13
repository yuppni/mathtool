from argparse import *
from calc.series import FORMULAS
from calc.integration import FUNCTIONS


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

    # Возвращаем настроенный разборщик в mathtool.py
    return parser