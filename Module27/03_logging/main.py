import datetime
import functools
from typing import Callable, Any


def logging(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'\nВызывается функция {func.__name__}\nДокументация:\n{func.__doc__}')
        try:
            result = func(*args, **kwargs)
            return result
        except BaseException as msg:
            with open('function_errors.log', 'a') as file:
                file.write(
                    f'Функция {func.__name__} Ошибка: {msg} возникла {datetime.datetime.now().strftime("%d-%m-%Y в %H-%M час.")}\n')

    return wrapped_func


@logging
def test():
    """
    Просто выводит сообщение на экран.

    """
    print('<Тут что-то происходит...>')


@logging
def calculating_math_func(data, fact_result={}):
    """
    Функция, которая делает следующие действия с входными данными:
1. Берёт факториал от числа.
2. Результат делит на куб входного числа.
3. И получившиеся число возводит в 10 степень.

    """
    if data in fact_result.keys():
        result = fact_result[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
            fact_result[index] = result

    result /= data ** 3
    result = result ** 10
    return result


test()

calculating_math_func(10)

# зачёт!
