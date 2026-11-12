from math import *

MAX_COUNT = 20
MAX_ABS = 10000


# Проверка списка перед вычислениями
def validate(values):
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
    return len(values)


# Накапливаем сумму всех чисел
def total(values):
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    return total(values) / len(values)


# Сумма квадратов самих чисел
def sum_squares(values):
    result = 0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    return sqrt(sum_squares(values) / len(values))


# Сначала среднее, затем сумма квадратов отклонений от него
def squared_deviations(values):
    average = mean(values)
    result = 0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    return squared_deviations(values) / len(values)


# СКО: деление на N уже выполнено в variance
def population_std(values):
    return sqrt(variance(values))


# Стандартное отклонение: делим на N - 1
def sample_std(values):
    if len(values) < 2:
        return None
    return sqrt(squared_deviations(values) / (len(values) - 1))


# Начинаем с первого числа, а не с нуля
def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def positive_count(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def negative_count(values):
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