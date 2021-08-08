import functools
import time
import datetime
from typing import Callable


def timer(func: Callable, name, form) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print(f'- Запускается {name}. Дата и время запуска: {datetime.datetime.now().strftime(form)}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'- Завершение {name}, время работы = {round(end - start, 3)}s')
        return result

    return wrapped


def log_methods(form, decorator=timer) -> Callable:
    for sym in form:
        if sym.isalpha():
            form = form.replace(sym, '%' + sym)

    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                cur_method = getattr(cls, i_method)
                name = f'{cls.__name__}.{cur_method.__name__}'
                decorated_method = decorator(cur_method, name, form)
                setattr(cls, i_method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# зачёт!
