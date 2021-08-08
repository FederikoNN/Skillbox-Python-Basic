import functools
from typing import Callable

app = {}


def callback(key: str):
    def callback_wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper():
            app[key] = func

        return wrapper

    return callback_wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


example()

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


