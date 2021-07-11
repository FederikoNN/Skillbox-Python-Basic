def file_data_view(file):
    file_data = open(file)
    print('\nСодержимое файла {}:'.format(file))
    print(file_data.read())
    file_data.close()


result_dict = {}
letters_count = 0
file_data_view('text.txt')

data_string = open('text.txt', 'r').read().lower()
for letter in data_string:
    if letter not in result_dict.keys() and letter.isalpha():
        letters_count += data_string.count(letter)
        result_dict[letter] = data_string.count(letter)

result_list_tpl = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))
file_out = open('analysis.txt', 'w')
for (key, value) in result_list_tpl:
    file_out.write('{} {}\n'.format(key, round(value / letters_count, 3)))
file_out.close()
file_data_view('analysis.txt')

# зачёт!
