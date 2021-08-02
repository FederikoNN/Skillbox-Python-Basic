import functools
from typing import Callable, Any

func_call = {}


def counter(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        if func.__name__ not in func_call.keys():
            func_call[func.__name__] = 1
        else:
            func_call[func.__name__] += 1
        print(f'\nРаботает функция {func.__name__}:\n')
        result = func(*args, **kwargs)
        print(f'\nФункция {func.__name__} была вызвана {func_call[func.__name__]} раз(а).')
        return result

    return wrapped_func


@counter
def test():
    print('<Тут что-то происходит...>')


@counter
def print_number(num):
    if num == 0:
        return
    for i_num in range(num):
        print(i_num)


test()
print_number(3)
test()
print_number(3)
test()
print('\nОбщее количество вызовов функций:\n')
for key, value in func_call.items():
    print(f'Функция {key} была вызвана {value} раз(а).')
