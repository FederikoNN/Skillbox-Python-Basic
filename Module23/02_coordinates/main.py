import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Попытка деления на ноль в первой функции')
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Попытка деления на ноль во второй функции')
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError as msg:
                print(msg)
                # TODO, если функции отработали с ошибкой, предлагаю создавать переменные res1 и res2 в блоках except.
                #  Таким образом, мы сможем избежать ошибок в коде ниже.

            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError as msg:
                print(msg)
            number = random.randint(0, 100)
            with open('result.txt', 'a') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(' | '.join(str(elem) for elem in my_list) + '\n')

except FileNotFoundError:
    print('Файл, который пытаетесь открыть для чтения, не существует')
except BaseException:
    print('Что-то пошло не так...')
