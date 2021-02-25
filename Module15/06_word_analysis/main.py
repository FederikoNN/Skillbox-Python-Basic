word = input('Введите слово: ')
unique_letters = 0
word_by_sym = list(word)

for sym_1 in word_by_sym:
    words_count = 0
    for sym_2 in word_by_sym:
        if sym_1 == sym_2:
            words_count += 1
    if words_count == 1:
        unique_letters += 1
print('Кол-во уникальных букв:', unique_letters)

# зачёт!
