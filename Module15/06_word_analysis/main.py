word = input('Введите слово: ')
unique_letters = len(word)
word_by_sym = list(word)
for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word_by_sym[i] == word_by_sym[j]:
            word_by_sym[j] += str(j)
            unique_letters -= 1
print('Кол-во уникальных букв:', unique_letters)
