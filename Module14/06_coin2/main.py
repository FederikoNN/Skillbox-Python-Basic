import math


def check(x, y, radius):
    a = math.sqrt(x ** 2 + y ** 2)
    if a <= radius:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


x = float(input('Введите координату х: '))
y = float(input('Введите координату y: '))
radius = float(input('Введите радиус: '))
check(x, y, radius)
