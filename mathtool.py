from sys import * #импорт необходимых функций для работы с системными параметрами
from calc.equation import *
from calc.stats import validate as validate_stats, REPORT
from calc.series import *
from calc.integration import FUNCTIONS, integrate, validate as validate_integral
from cli import create_parser

def handle_solve(args):
    # Коэффициенты должны быть заданы все вместе либо отсутствовать
    coefficients = (args.a, args.b, args.c)

    if all(value is None for value in coefficients):
        try:
            A = int(input("Введите коэффициент A: "))
            B = int(input("Введите коэффициент B: "))
            C = int(input("Введите коэффициент C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif any(value is None for value in coefficients):
        raise ValueError("укажите все три коэффициента либо ни одного")
    else:
        A, B, C = coefficients

    kind, D, roots = solve(A, B, C)

    if kind == "квадратное":
        print("Уравнение является квадратным")
        print(f"Дискриминант: D = {D}")

        if len(roots) == 2:
            print(f"Корни уравнения: x1 = {roots[0]:.3f}, x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"Уравнение имеет один корень: x = {roots[0]:.3f}")
        else:
            print("Уравнение не имеет действительных корней")
    else:
        print("Уравнение является линейным")
        print(f"Корень уравнения: x = {roots[0]:.3f}")

    return 0

# Читаем числа из переданного источника
def read_numbers(source):
    values = []

    for line in source:
        for word in line.split():
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом")
            values.append(value)

    validate_stats(values)
    return values


def handle_stats(args):
    # Файл автоматически закроется после чтения
    if args.input is not None:
        with open(args.input, encoding="utf-8-sig") as source:
            values = read_numbers(source)
    else:
        values = read_numbers(stdin)

    # Получаем функции и форматы из таблицы
    for label, function, form in REPORT:
        value = function(values)

        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0

def handle_series(args):
    # Получаем функцию слагаемого и запись формулы
    term, formula = FORMULAS[args.func]

    if args.terms is not None:
        result = sum_by_terms(term, args.terms)
        count = args.terms
    else:
        result, count = sum_by_eps(term, args.eps)

    # Печатаем только после успешной проверки и расчёта
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{DIGITS}f}")

    return 0

def handle_integrate(args):
    # Получаем функцию, формулу и допустимые границы
    F, formula, low, high, inclusive = FUNCTIONS[args.func]

    validate_integral(
        args.start, args.end, args.steps, low, high, inclusive
    )
    result = integrate(F, args.start, args.end, args.steps)

    # Выводим только после успешной проверки и расчёта
    print(formula)
    print(f"Значение интеграла: {result:.4f}")

    return 0
# Каждой команде соответствует свой обработчик
HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


def main(argv):
    parser = create_parser()
    args = parser.parse_args(argv)

    # Без команды выводим общую справку
    if args.command is None:
        parser.print_help()
        return 0

    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=stderr)
        return 1


# Запускаем программу только при прямом запуске файла
if __name__ == "__main__":
    exit(main(argv[1:]))

