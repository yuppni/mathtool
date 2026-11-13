from math import *

MAX_STEPS = 100000


def ratio(x):
    """Возвращает значение функции x / (x + 1) в точке x."""
    return x / (x + 1)


def root(x):
    """Возвращает значение функции sqrt(x^2 + 1) в точке x."""
    return sqrt(x * x + 1)


# Функция, формула, нижняя и верхняя границы,
# признак того, что сами границы разрешены
FUNCTIONS = {
    "ratio": (ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


# Проверяем параметры до вычисления и вывода формулы
def validate(a, b, steps, low, high, inclusive):
    """Проверяет пределы, число шагов и принадлежность промежутку с учётом включения границ."""
    if not isfinite(a) or not isfinite(b):
        raise ValueError("пределы должны быть конечными числами")

    if a >= b:
        raise ValueError("начальный предел не меньше конечного")

    for value in (a, b):
        if inclusive:
            if value < low or value > high:
                raise ValueError("предел вне промежутка")
        else:
            if value <= low or value >= high:
                raise ValueError("предел вне промежутка")

    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


# Общий расчёт: формула передаётся параметром F
def integrate(F, a, b, steps):
    """Возвращает интеграл функции F от a до b методом левых прямоугольников за steps шагов."""
    dx = (b - a) / steps
    result = 0

    for i in range(steps):
        # Левая граница очередного прямоугольника
        x = a + i * dx
        result += F(x) * dx

    return result