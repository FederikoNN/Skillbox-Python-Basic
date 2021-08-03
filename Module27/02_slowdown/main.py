import functools
import time
from typing import Callable, Any


def slowdown(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        time.sleep(10)
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@slowdown
def test():
    print('<Тут что-то происходит...>')


@slowdown
def print_number(num):
    if num == 0:
        return
    for i_num in range(num):
        print(i_num)


test()

print_number(3)

# зачёт!
