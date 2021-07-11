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

file_in.close()
file_out.close()
print('\n\nСодержимое файла cipher_text.txt:')
print(open('cipher_text.txt').read())
