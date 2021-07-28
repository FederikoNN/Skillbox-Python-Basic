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


for files_path in gen_files_path(folder='PycharmProjects', path='C:/Users/'):
    print(files_path)
