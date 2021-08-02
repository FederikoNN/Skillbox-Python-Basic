import functools
import time
from typing import Callable, Any


def slowdown(func: Callable) -> Any:
    top = True

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        nonlocal top
        if top:
            top = False
            time.sleep(10)
            result = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
            top = True
        return result

    return wrapped_func


@slowdown
def test():
    print('<Тут что-то происходит...>')


@slowdown
def print_number(num):
    if num == 0:
        return
    print_number(num - 1)
    print(num)


test()

print_number(3)
