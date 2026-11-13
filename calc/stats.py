from math import *

MAX_COUNT = 20
MAX_ABS = 10000


# Проверка списка перед вычислениями
def validate(values):
    """Проверяет количество и допустимость чисел; при ошибке вызывает ValueError."""
    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError("количество чисел превышает 20")

    for value in values:
        if not isfinite(value):
            raise ValueError("число должно быть конечным")
        if abs(value) > MAX_ABS:
            raise ValueError("число вне допустимого диапазона")


def count(values):
    """Возвращает количество чисел в списке."""
    return len(values)


# Накапливаем сумму всех чисел
def total(values):
    """Возвращает сумму чисел списка."""
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    """Возвращает среднее арифметическое чисел списка."""
    return total(values) / len(values)


# Сумма квадратов самих чисел
def sum_squares(values):
    """Возвращает сумму квадратов чисел списка."""
    result = 0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    """Возвращает квадратный корень из среднего квадратов чисел списка."""
    return sqrt(sum_squares(values) / len(values))


# Сначала среднее, затем сумма квадратов отклонений от него
def squared_deviations(values):
    """Возвращает сумму квадратов отклонений чисел списка от их среднего."""
    average = mean(values)
    result = 0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    """Возвращает дисперсию с делением суммы квадратов отклонений на N."""
    return squared_deviations(values) / len(values)


# СКО: деление на N уже выполнено в variance
def population_std(values):
    """Возвращает СКО — квадратный корень из дисперсии."""
    return sqrt(variance(values))


# Стандартное отклонение: делим на N - 1
def sample_std(values):
    """Возвращает стандартное отклонение с делением суммы квадратов отклонений на N - 1."""
    if len(values) < 2:
        return None
    return sqrt(squared_deviations(values) / (len(values) - 1))


# Начинаем с первого числа, а не с нуля
def minimum(values):
    """Возвращает наименьшее число в списке."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Возвращает наибольшее число в списке."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def positive_count(values):
    """Возвращает количество положительных чисел в списке."""
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def negative_count(values):
    """Возвращает количество отрицательных чисел в списке."""
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


# Подпись, функция расчёта, формат вывода
# Без скобок передаём саму функцию, пока не вызывая её
REPORT = [
    ("Количество", count, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", sum_squares, ".3f"),
    ("Ср. кв.", root_mean_square, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", population_std, ".3f"),
    ("Станд. откл.", sample_std, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", positive_count, "d"),
    ("Отрицательных", negative_count, "d"),
]