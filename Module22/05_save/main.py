import os


def enter_data_control():
    while True:
        folders = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
        path_to_folder = os.path.sep
        for i_folders in folders:
            path_to_folder = os.path.join(path_to_folder, i_folders)
        if os.path.exists(path_to_folder):
            return path_to_folder
        else:
            print('Ошибка ввода пути к каталогу!\nПопробуйте ещё раз.')


def save_to_file(path, file, string):
    msg = 'сохранён'
    path_to_file = os.path.join(path, file)
    if os.path.exists(path_to_file):
        choice = input('Вы действительно хотите перезаписать файл? ')
        msg = 'перезаписан'
        if choice.lower() != 'да':
            print('Не удалось завершить операцию!')
            return
    file_in = open(path_to_file, 'w+')
    file_in.write(string)
    print(f'Файл успешно {msg}!\n')
    print('Содержимое файла:')
    file_in.seek(0)
    print(file_in.read())
    file_in.close()


text = input('Введите строку: ')
path_out = enter_data_control()
file_save = input('Введите имя файла: ') + '.txt'
save_to_file(path_out, file_save, text)
