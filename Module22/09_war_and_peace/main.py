import zipfile


def dict_append(dict, string):
    for letter in string:
        if letter in dict.keys():
            dict[letter] += 1
        elif letter.isalpha():
            dict[letter] = 1

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

# зачёт!
