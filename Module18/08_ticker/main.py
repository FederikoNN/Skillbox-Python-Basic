def string_compare(string1, string2):
    for index_string2 in range(len(string2)):
        if string1.find(string2) == 0:
            return index_string2
        else:
            string2 = string2[1:] + string2[:1]
    return -1


string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')

if string_compare(string_1, string_2) != -1:
    print('Первая строка получается из второй со сдвигом', string_compare(string_1, string_2))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
