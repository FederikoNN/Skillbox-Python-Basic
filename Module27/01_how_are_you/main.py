from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    top = True

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        nonlocal top
        if top:
            top = False
            input('Как дела?')
            print('А у меня не очень! Ладно, держи свою функцию.')
            result = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
            top = True
        return result

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def print_number(num):
    if num == 0:
        return
    print_number(num - 1)
    print(num)


test()

print_number(3)
