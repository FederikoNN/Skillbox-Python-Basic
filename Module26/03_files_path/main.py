import os.path


def gen_files_path(folder: str, path=os.path.abspath(os.sep)) -> str:
    for elem in os.listdir(path):
        path_elem = os.path.join(os.path.abspath(path), elem)
        if os.path.isfile(path_elem):
            print(path_elem)
            continue
        elif folder == elem:
            print(f'\nКаталог {folder} найден.\nПуть к каталогу: {path_elem}')
            return path_elem
        else:
            path_elem = gen_files_path(folder=folder, path=path_elem)
            if path_elem:
                return path_elem


path_search = input('Введите путь для поиска: ')
folder_search = input('Какой каталог ищем? ')
print('\nПути всех встреченных файлов:\n')
if not gen_files_path(folder=folder_search, path=path_search):
    print(f'\nКаталог {folder_search} не найден.')

# зачёт!
