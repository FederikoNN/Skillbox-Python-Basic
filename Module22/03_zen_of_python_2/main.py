words_num = 0
sym_num = 0
sym_min = ''
file = open('zen.txt', 'r')
zen_in = file.readlines()
lines_num = len(zen_in)
sym_min_num = len((''.join(''.join(zen_in).split())))
print('Количество строк:', lines_num)
for word in ''.join(zen_in).split():
    if word[0].isalpha():
        words_num += 1
    for sym in word:
        if sym.isalpha():
            sym_num += 1
            # TODO, предлагаю упростить строку ниже. Если мы используем её для поиска буквы с минимальным количеством повторений,
            #  В таком случае, предлагаю попробовать изначально создать словарь, в котором мы будем производить
            #  подсчёт количества каждой буквы отдельно.
            if (''.join(''.join(zen_in).split())).lower().count(sym.lower()) < sym_min_num:
                sym_min_num = (''.join(''.join(zen_in).split())).count(sym.lower())
                sym_min = sym.lower()
print('Количество слов:', words_num)
print('Количество букв:', sym_num)
print('Меньше всего (' + str(sym_min_num), 'вхождения) встречается буква:', sym_min, '(без учёта регистра)')

file.close()
