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

def earlier(a, b, descending):
    """Возвращает True, если a должно стоять раньше b."""
    return out_of_order(b, a, descending)


def quick(values, descending=False):
    """Сортирует список методом Хоара на месте и возвращает None."""
    quick_part(values, 0, len(values) - 1, descending)


def quick_part(values, left, right, descending):
    """Упорядочивает участок, рекурсивно обрабатывая меньшую часть."""
    while left < right:
        pivot = values[(left + right) // 2]
        i = left
        j = right

        # Разделяем участок относительно опорного значения
        while i <= j:
            while earlier(values[i], pivot, descending):
                i += 1

            while earlier(pivot, values[j], descending):
                j -= 1

            if i <= j:
                values[i], values[j] = values[j], values[i]
                i += 1
                j -= 1

        # Меньшую часть обрабатываем рекурсивно,
        # большую — следующей итерацией цикла
        if j - left < right - i:
            quick_part(values, left, j, descending)
            left = i
        else:
            quick_part(values, i, right, descending)
            right = j


def merge(values, descending=False):
    """Сортирует список слиянием на месте и возвращает None."""
    merge_part(values, 0, len(values) - 1, descending)


def merge_part(values, left, right, descending):
    """Разделяет участок, сортирует половины и объединяет их."""
    if left >= right:
        return

    middle = (left + right) // 2

    merge_part(values, left, middle, descending)
    merge_part(values, middle + 1, right, descending)
    merge_halves(values, left, middle, right, descending)


def merge_halves(values, left, middle, right, descending):
    """Сливает два соседних упорядоченных участка."""
    result = []
    i = left
    j = middle + 1

    # При равенстве первым берём элемент левой половины
    while i <= middle and j <= right:
        if earlier(values[j], values[i], descending):
            result.append(values[j])
            j += 1
        else:
            result.append(values[i])
            i += 1

    # Добавляем оставшиеся элементы
    result.extend(values[i:middle + 1])
    result.extend(values[j:right + 1])

    values[left:right + 1] = result


def sift(values, i, size, descending):
    """Восстанавливает свойство кучи просеиванием элемента вниз."""
    while True:
        selected = i

        # Проверяем левого и правого потомка
        for child in (2 * i + 1, 2 * i + 2):
            if child < size:
                if earlier(values[selected], values[child], descending):
                    selected = child

        if selected == i:
            return

        values[i], values[selected] = values[selected], values[i]
        i = selected


def heap(values, descending=False):
    """Сортирует список пирамидальным методом и возвращает None."""
    n = len(values)

    # Строим кучу начиная с последних родительских узлов
    for i in range(n // 2 - 1, -1, -1):
        sift(values, i, n, descending)

    # Переносим корень в конец и уменьшаем рабочую часть
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        sift(values, 0, end, descending)

# Название метода и соответствующая функция
METHODS = {
    "bubble": bubble,
    "selection": selection,
    "insertion": insertion,
    "counting": counting,
    "quick": quick,
    "merge": merge,
    "heap": heap,
}