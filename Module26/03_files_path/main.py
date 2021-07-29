import os.path


def gen_files_path(folder: str, path=os.path.abspath(os.sep)) -> str:
    for elem in os.listdir(path):
        path_elem = os.path.join(path, elem)
        if os.path.isdir(path_elem) and elem == folder:
            print(f'Каталог {folder} найден.')
            return
        if os.path.isfile(path_elem):
            yield path_elem
    print(f'Каталог {folder} не найден.')


# TODO,
#  1. Пожалуйста, добавьте запросы ввода пользователя.
#  2. Стоит реализовать функцию с использованием рекурсии, но без использования os.walk.
#  При вводе
#  path = C:\Users\...\python_basic
#  folder = 02_refactoring
#  Наша функция должна найти нужную папку =)

for files_path in gen_files_path(folder='PycharmProjects', path='C:/Users/'):
    print(files_path)
