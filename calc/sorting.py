from calc.arrays import MIN_VALUE, MAX_VALUE


def out_of_order(a, b, descending):
    """Возвращает True, если два значения стоят в неправильном порядке."""
    if descending:
        return a < b
    return a > b


def bubble(values, descending=False):
    """Сортирует список пузырьком на месте и возвращает None."""
    n = len(values)

    for i in range(n - 1):
        swapped = False

        # После каждого прохода последний элемент уже на своём месте
        for j in range(n - 1 - i):
            if out_of_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        # Если обменов не было, список уже упорядочен
        if not swapped:
            break


def selection(values, descending=False):
    """Сортирует список выбором на месте и возвращает None."""
    n = len(values)

    for i in range(n - 1):
        best = i

        # Ищем элемент, который должен стоять на позиции i
        for j in range(i + 1, n):
            if out_of_order(values[best], values[j], descending):
                best = j

        values[i], values[best] = values[best], values[i]


def insertion(values, descending=False):
    """Сортирует список вставками на месте и возвращает None."""
    n = len(values)

    for i in range(1, n):
        current = values[i]
        j = i

        # Сдвигаем элементы, освобождая место для current
        while j > 0 and out_of_order(values[j - 1], current, descending):
            values[j] = values[j - 1]
            j -= 1

        values[j] = current


def counting(values, descending=False):
    """Сортирует список подсчётом на месте и возвращает None."""
    counts = [0] * (MAX_VALUE - MIN_VALUE + 1)

    # Считаем количество появлений каждого значения
    for value in values:
        counts[value - MIN_VALUE] += 1

    # Выбираем направление обхода счётчиков
    if descending:
        indices = range(len(counts) - 1, -1, -1)
    else:
        indices = range(len(counts))

    # Записываем значения обратно в исходный список
    k = 0

    for index in indices:
        for _ in range(counts[index]):
            values[k] = index + MIN_VALUE
            k += 1


# Название метода и соответствующая функция
METHODS = {
    "bubble": bubble,
    "selection": selection,
    "insertion": insertion,
    "counting": counting,
}