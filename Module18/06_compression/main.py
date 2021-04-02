string_in = input('Введите строку: ')
string_out = ''
letter_tmp = string_in[:1]
# a = string_in.count('a')
# print(letter_tmp, a)
count = 1
for sym in string_in[1:]:
    if letter_tmp == sym:
        count += 1
    else:
        string_out += letter_tmp + str(count)
        letter_tmp = sym
        count = 1
string_out += letter_tmp + str(count)

print('Закодированная строка: ', string_out)

# зачёт!
