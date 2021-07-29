import os
from collections.abc import Iterable


def sum_string_code(path: str = '.') -> Iterable[int]:
    for elem in os.listdir(path):
        string_count = 0
        path_file = os.path.join(path, elem)
        if os.path.isfile(path_file) and elem.endswith('.py'):
            with open(path_file, 'r') as file:
                for line in file:
                    line = line.strip(' \n')
                    if not line.startswith('#') and line:
                        string_count += 1
            yield string_count


path_in = input('Введите путь к каталогу ("."- текущий каталог): ')
# for i in sum_string_code(path=path_in):
#     print(i)
print(f'Общее количество строк кода в питоновских файлах, расположенных в директории {os.path.abspath(path_in)}: '
      f'{sum(sum_string_code(path=path_in))}')
# print(sum(sum_string_code()))
