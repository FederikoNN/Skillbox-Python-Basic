import os


def save(string):
    folders = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    file_save = input('Введите имя файла: ') + '.txt'
    path_to_folder = os.path.sep
    for i_folders in folders:
        path_to_folder = os.path.join(path_to_folder, i_folders)
        if not os.path.exists(path_to_folder):
            print('Каталога', i_folders, 'не существует!')
    path_to_file = os.path.join(path_to_folder, file_save)
    if os.path.exists(path_to_file):
        choice = input('Вы действительно хотите перезаписать файл? ')
        if choice.lower() != 'да':
            print('Не удалось завершить операцию!')
            return
    file_in = open(path_to_file, 'w')
    file_in.write(string)
    file_in.close()
    if os.path.getsize(path_to_file) > 0:
        print('Файл успешно сохранён!')
        print('Содержимое файла:')
        file_out = open(path_to_file, 'r')
        print(file_out.read())
        file_out.close()

    return

text = input('Введите строку: ')
save(text)
