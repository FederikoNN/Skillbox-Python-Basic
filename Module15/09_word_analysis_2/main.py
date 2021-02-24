word = input('Введите слово: ')
word_sym = list(word)
word_reverse = ''
for i in range(len(word)):
    word_reverse += word_sym[-(i + 1)]
if word == word_reverse:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
