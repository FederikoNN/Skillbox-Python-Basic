import zipfile


def dict_append(dict, string, dict_string={}):
    # TODO, подсчёт данных в словаре, предлагаю реализовать одним циклом с проверкой,
    #  является текущий символ строки буквой.
    #  Если является, то стоит проверить наличие буквы в словаре, если есть,
    #  то +1 к счётчику, если нет, то создаём новый кюч со значением 1.
    #  count в решении лишний, т.к. внутри содержит цикл. Получается, что одну и туже букву мы вычисляем несколько раз.
    #  К примеру, к букве "o" мы применили метод count 262119 раз =)
    for letter in string:
        if letter not in dict_string.keys() and letter.isalpha():
            dict_string[letter] = string.count(letter)
    for key in dict_string.keys():
        if key in dict.keys():
            dict[key] = dict[key] + dict_string[key]
        else:
            dict[key] = dict_string[key]
    dict_string.clear()
    return dict


zipfile.ZipFile('voyna-i-mir.zip', 'r').extractall()
file_in = open('voyna-i-mir.txt', 'r', encoding='utf-8')
dict_result = {}
for line in file_in.readlines():
    if line:
        dict_append(dict_result, line)

result_list_tpl = sorted(dict_result.items(), key=lambda x: (-x[1], x[0]))
for (key, value) in result_list_tpl:
    print('Буква "{}"; количество вхождений:\t{}'.format(key, value))
