import sys
import math

MAX_VALUE = 10000 #огранчение коэфициентов

def print_help():
    """Вывод справки."""
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("  python mathtool.py              вывод справки")
    print("  python mathtool.py --help       вывод справки")
    print("  python mathtool.py solve        ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2")
    print("                                  решение с заданными коэффициентами")
    print()
    print("Коэффициенты A, B, C — целые числа,")
    print("по модулю не превышающие 10000.")

def get_from_keyboard():
    """Получение коэффициентов с клавиатуры."""
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
        return a, b, c
    except ValueError:
        print(
            "ОШИБКА: коэффициент не является целым числом",
            file=sys.stderr
        )
        sys.exit(1)

def get_coefficients_from_arguments(args):
    """Получение коэффициентов из параметров командной строки."""
    if len(args) != 6:
        print(
            "ОШИБКА: неверный набор параметров",
            file=sys.stderr
        )
        sys.exit(1)

    if args[0] != "-a" or args[2] != "-b" or args[4] != "-c":
        print(
            "ОШИБКА: неизвестный параметр",
            file=sys.stderr
        )
        sys.exit(1)

    try:
        a = int(args[1])
        b = int(args[3])
        c = int(args[5])
        return a, b, c
    except ValueError:
        print(
            "ОШИБКА: коэффициент не является целым числом",
            file=sys.stderr
        )
        sys.exit(1)

def check_coefficients(a, b, c):
    """Проверка диапазона коэффициентов."""
    if (
        abs(a) > MAX_VALUE
        or abs(b) > MAX_VALUE
        or abs(c) > MAX_VALUE
    ):
        print(
            "ОШИБКА: значение вне допустимого диапазона",
            file=sys.stderr
        )
        sys.exit(1)

def solve_equation(a, b, c):
    """Определение вида уравнения и поиск действительных корней."""

    # Линейное уравнение или отсутствие уравнения
    if a == 0:
        if b == 0:
            print(
                "ОШИБКА: это не уравнение, неизвестное отсутствует",
                file=sys.stderr
            )
            sys.exit(1)

        print("Уравнение линейное")

        x = -c / b
        print(f"x = {x:.3f}")
        return

    # Квадратное уравнение
    print("Уравнение квадратное")

    discriminant = b * b - 4 * a * c
    print(f"D = {discriminant}")

    if discriminant > 0:
        sqrt_d = math.sqrt(discriminant)

        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")

    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")

    else:
        print("Действительных корней нет")

def main():
    """Основная функция программы."""

    args = sys.argv[1:]

    # Нет параметров или указан --help
    if len(args) == 0 or args[0] == "--help":
        print_help()
        return 0

    # Проверка команды
    if args[0] != "solve":
        print(
            "ОШИБКА: неизвестная команда",
            file=sys.stderr
        )
        return 1

    # solve без коэффициентов
    if len(args) == 1:
        a, b, c = get_coefficients_from_keyboard()

    # solve -a ... -b ... -c ...
    elif len(args) == 7:
        a, b, c = get_coefficients_from_arguments(args[1:])

    else:
        print(
            "ОШИБКА: неверный набор параметров",
            file=sys.stderr
        )
        return 1

    # Проверка диапазона
    check_coefficients(a, b, c)

    # Решение
    solve_equation(a, b, c)

    return 0

if __name__ == "__main__":
    sys.exit(main())