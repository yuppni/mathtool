from math import * #импорт необходимых математических функций
from sys import * #импорт необходимых функций для работы с системными параметрами
from calc.equation import *

MAX_VALUE = 10000 #ограничение коэфициентов

def spravka(): #функция вывода справки
    print('Данное приложение решает уравнение вида A*x^2 + B*x + C = 0')
    print('Правила использования:')
    print('Для вывода справки введите: python mathtool.py или python mathtool.py --help')
    print('Для ввода коэффициентов с клавиатуры введите: python mathtool.py solve')
    print('Для решения с заданными коэффициентами введите: python mathtool.py solve -a 1 -b -3 -c 2')
    print(f'Коэффициенты должны быть целыми числами в диапазоне от {-1 * MAX_VALUE} до {MAX_VALUE}')
    exit(0) #завершение работы программы без ошибок

if len(argv) == 1 or argv[1] == '--help': #если аргументов нет или введена команда --help вывод справк
    spravka() 

if len(argv) > 1 and argv[1] != 'solve' and argv[1] != '--help':
    print('ОШИБКА: неизвестная команда', file=stderr)
    exit(1)

if argv[1] == 'solve':
    if len(argv) == 2: #если введена команда solve без аргументов, то запрашиваем коэффициенты у пользователя
        try:
            A = int(input('Введите коэффициент A: ')) 
            B = int(input('Введите коэффициент B: ')) 
            C = int(input('Введите коэффициент C: ')) 
        except ValueError:
            print('ОШИБКА: коэффициент не является целым числом', file=stderr)
            exit(1)
    elif len(argv) == 8: #если введена команда solve с аргументами, то извлекаем коэффициенты из аргументов
            if argv[2] == '-a' and argv[4] == '-b' and argv[6] == '-c':
                try:
                    A = int(argv[3]) 
                    B = int(argv[5]) 
                    C = int(argv[7]) 
                except ValueError:
                    print('ОШИБКА: коэффициент не является целым числом', file=stderr)
                    exit(1)
            else:
                print('ОШИБКА: неверный формат аргументов', file=stderr)
                exit(1)
    else:
        print('ОШИБКА: неверный набор параметров', file=stderr)
        exit(1)
    if abs(A) > MAX_VALUE or abs(B) > MAX_VALUE or abs(C) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=stderr)
        exit(1)
try:
    kind, D, roots = solve(A, B, C)
except ValueError as error:
    print(f"ОШИБКА: {error}", file=stderr)
    exit(1)

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