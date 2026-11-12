from math import *

MAX_VALUE = 10000  # ограничение коэффициентов


def validate(A, B, C):
    if abs(A) > MAX_VALUE:
        raise ValueError("коэффициент A вне допустимого диапазона")

    if abs(B) > MAX_VALUE:
        raise ValueError("коэффициент B вне допустимого диапазона")

    if abs(C) > MAX_VALUE:
        raise ValueError("коэффициент C вне допустимого диапазона")

    if A == 0 and B == 0:
        raise ValueError("выражение не является уравнением (A и B равны нулю)")


def solve(A, B, C):
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