import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator):
    def decorate(*args, **kwargs):
        # @functools.wraps(*args, **kwargs)
        def decorated(func):
            return decorator(func, *args, **kwargs)

        return decorated

    return decorate


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrap(*other_args, **other_kwargs):
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        result = func(*other_args, **other_kwargs)
        return result

    return wrap


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
