from math import *

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = ceil(-log10(MAX_EPS))


# Нечётные слагаемые положительные, чётные — отрицательные
def sign(n):
    """Возвращает 1 для нечётного номера слагаемого и −1 для чётного."""
    if n % 2 == 0:
        return -1
    return 1


# Слагаемое ряда 1/3 - 1/6 + 1/9 - ...
def third(n):
    """Возвращает слагаемое ряда third с номером n и чередующимся знаком."""
    return sign(n) / (3 * n)


# Слагаемое ряда 1/(1²+1) - 1/(2²+1) + ...
def sqplus(n):
    """Возвращает слагаемое ряда sqplus с номером n и чередующимся знаком."""
    return sign(n) / (n * n + 1)


# Название ряда: функция слагаемого и текст формулы
FORMULAS = {
    "third": (third, "S = 1/3 - 1/6 + 1/9 - ..."),
    "sqplus": (
    sqplus,"S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
}


# Складываем заданное количество слагаемых
def sum_by_terms(term, count):
    """Возвращает сумму заданного количества слагаемых ряда."""
    if not 1 <= count <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")

    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result


# Складываем до достижения заданной точности
def sum_by_eps(term, eps):
    if not isfinite(eps) or not 0 < eps <= MAX_EPS:
        raise ValueError("точность вне диапазона")

    result = 0
    n = 0

    while True:
        n += 1
        value = term(n)
        result += value

        # Последнее слагаемое тоже включаем в сумму
        if abs(value) < eps:
            return result, n

        # Защита от слишком долгого вычисления
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")