file_name = input('Введите название файла: ')
forbidden_symbols = '@№$%^&*()'

if file_name[0] in forbidden_symbols:
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
