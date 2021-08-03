from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    top = True

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def print_number(num):
    if num == 0:
        return
    for i_num in range(num):
        print(i_num)


test()

print_number(3)
