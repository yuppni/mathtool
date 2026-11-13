from math import *

MAX_VALUE = 10000  # ограничение коэффициентов


def validate(A, B, C):
    """Проверяет диапазон коэффициентов и наличие неизвестного; при ошибке вызывает ValueError."""
    # Проверяем каждый коэффициент одним циклом
    coefficients = {"A": A, "B": B, "C": C} #создаём словарь с коэффициентами для проверки

    for name, value in coefficients.items(): 
        if abs(value) > MAX_VALUE:
            raise ValueError(
                f"коэффициент {name} вне допустимого диапазона"
            )

    if A == 0 and B == 0:
        raise ValueError(
            "выражение не является уравнением (A и B равны нулю)"
        )

def solve(A, B, C):
    """Возвращает вид уравнения, дискриминант и список действительных корней."""
    validate(A, B, C)

    if A != 0:
        D = B**2 - 4*A*C  # вычисление дискриминанта

        if D > 0:
            x1 = (-B + sqrt(D)) / (2*A)
            x2 = (-B - sqrt(D)) / (2*A)
            return "квадратное", D, [x1, x2]

        elif D == 0:
            x = -B / (2*A)
            return "квадратное", D, [x]

        else:
            return "квадратное", D, []

    else:
        x = -C / B  # вычисление корня линейного уравнения
        return "линейное", None, [x]