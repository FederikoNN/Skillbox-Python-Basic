import functools
from typing import Callable, Any


def debug(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        args_str = ", ".join(
            [f'{arg}' if isinstance(arg, int) else f'"{arg}"' for arg in args])
        kwargs_str = ", ".join(
            [key + "=" + str(value) if isinstance(value, int) else f'{key}="{value}"' for key, value in kwargs.items()])
        print(
            f'\nВызывается {func.__name__}({", ".join([args_str, kwargs_str]).strip(" ,")})')
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула значение '{result}'")
        print(result)
        return result

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачёт!
