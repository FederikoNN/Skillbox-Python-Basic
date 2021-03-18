alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

text_crypto = [(alphabet[(alphabet.index(letter) + shift) % 33] if alphabet.count(letter) != 0 else letter) for letter
               in text]
print("".join(text_crypto))
