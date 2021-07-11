alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar_cipher(string, data):
    # string = string.lower()
    return ([(alphabet[(alphabet.index(letter) + data) % 26] if alphabet.count(letter) != 0 else letter) for letter in
             string.lower()])


file_in = open('text.txt', 'r')
file_out = open('cipher_text.txt', 'w')
shift = 1
print('Содержимое файла text.txt:')
for line in file_in:
    print(line, end='')
    file_out.write(''.join(caesar_cipher(line, shift)).capitalize())
    shift += 1


# TODO, предлагаю не закрывать файл перед выводом текста.
#  Стоит открыть файл один раз в режим на запись и на чтение, после чего, после записи данных в файл,
#  перенести курсор в начало файла при помощи метода seek и произвести вывод данных.
#  В таком случае, закрывать и открывать файл повторно будет не нужно.
#  Все режимы открытия файлов можно посмотреть тут:
#  http://pythonicway.com/python-fileio


file_in.close()
file_out.close()
print('\n\nСодержимое файла cipher_text.txt:')
print(open('cipher_text.txt').read())
