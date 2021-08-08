import functools
from typing import Callable

user_permissions = ['admin']


def check_permission(user: str):
    def check_wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return check_wrapped


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
