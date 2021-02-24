word = input('Введите слово: ')
unique_letters = len(word)
word_by_sym = list(word)

# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word_by_sym[i] == word_by_sym[j]:
            word_by_sym[j] += str(j)
            unique_letters -= 1
print('Кол-во уникальных букв:', unique_letters)

# TODO Введите слово: карамба
#  Кол-во уникальных букв: 5
#  ПО идее, в слове "карамба" 4 уникальные буквы "к р м б"