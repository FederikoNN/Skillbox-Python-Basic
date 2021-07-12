words_num = 0
sym_num = {}
sym_min = ''
file = open('zen.txt', 'r')
zen_in = file.readlines()
lines_num = len(zen_in)
sym_min_num = len((''.join(''.join(zen_in).split())))
print('Количество строк:', lines_num)
for word in ''.join(zen_in).split():
    if word[0].isalpha():
        words_num += 1
    for sym in word.lower():
        if sym in sym_num:
            sym_num[sym] += 1
        elif sym.isalpha():
            sym_num[sym] = 1
sym_min_num = min(sym_num.values())
sym_num_list_tpl = sorted(sym_num.items(), key=lambda x: (x[1], x[0]))
sym_min = sym_num_list_tpl[0][0]
print('Количество слов:', words_num)
print('Количество букв:', sum(sym_num.values()))
print('Меньше всего (' + str(sym_min_num), 'вхождения) встречается буква:', sym_min, '(без учёта регистра)')

file.close()

# зачёт!
