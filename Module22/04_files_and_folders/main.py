import os


def dir_info(path, info=None):
    if info is None:
        info = {'Размер каталога (в Кб):': 0, 'Количество подкаталогов:': 0, 'Количество файлов:': 0}
    for i_elem in os.listdir(path):
        path_elem = os.path.join(path, i_elem)
        if os.path.isdir(path_elem):
            info['Количество подкаталогов:'] += 1
            dir_info(path_elem, info)
        else:
            info['Количество файлов:'] += 1
            info['Размер каталога (в Кб):'] += os.path.getsize(path_elem) / 1024

    return info


# path = 'C:/Users/fvk19/PycharmProjects/python_basic/Module21'
path = input('Введите путь к каталогу: ')
for key, value in dir_info(path).items():
    print(key, value)
