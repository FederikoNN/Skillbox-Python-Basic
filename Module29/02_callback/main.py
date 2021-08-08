import functools
from typing import Callable

app = {}


def callback(key: str):
    def callback_wrapped(func: Callable) -> Callable:

        # TODO, функцию было бы правильней добавлять в словарь в этом месте кода

        @functools.wraps(func)
        def wrapper():
            app[key] = func
            # TODO, стоит обязательно запустить функцию и вернуть её запуск.
            #  Иначе, результат работы функции потеряется в декораторе, если функция что-то возвращает.
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


