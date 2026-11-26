import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def validate(values):
    """Проверяет количество, целочисленность и диапазон элементов массива."""
    if not 1 <= len(values) <= MAX_COUNT:
        raise ValueError(
            f"количество элементов вне диапазона 1..{MAX_COUNT}"
        )

    for value in values:
        if not isinstance(value, int):
            raise ValueError("элемент массива должен быть целым числом")

        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(
                f"элемент массива вне диапазона {MIN_VALUE}..{MAX_VALUE}"
            )


def validate_fill(count, low, high):
    """Проверяет количество и границы значений для генерации массива."""
    if not 1 <= count <= MAX_COUNT:
        raise ValueError(
            f"количество элементов вне диапазона 1..{MAX_COUNT}"
        )

    if not MIN_VALUE <= low <= MAX_VALUE:
        raise ValueError(
            f"нижняя граница вне диапазона {MIN_VALUE}..{MAX_VALUE}"
        )

    if not MIN_VALUE <= high <= MAX_VALUE:
        raise ValueError(
            f"верхняя граница вне диапазона {MIN_VALUE}..{MAX_VALUE}"
        )

    if low > high:
        raise ValueError("нижняя граница больше верхней")


def fill(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Возвращает список случайных целых чисел с заданными границами и seed."""
    validate_fill(count, low, high)
    random.seed(seed)

    values = []

    for _ in range(count):
        values.append(random.randint(low, high))

    return values


def validate_search(value):
    """Проверяет допустимый диапазон искомого целого числа."""
    if abs(value) > MAX_SEARCH:
        raise ValueError(
            f"искомое значение вне диапазона {-MAX_SEARCH}..{MAX_SEARCH}"
        )


def validate_sorted(values):
    """Проверяет, что массив упорядочен по возрастанию с допустимыми повторами."""
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            raise ValueError("массив не упорядочен по возрастанию")


def binary_search(values, target):
    """Возвращает индекс target в упорядоченном массиве или None."""
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle

        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None