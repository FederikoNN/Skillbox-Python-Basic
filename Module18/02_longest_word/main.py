string = input('Введите строку: ').split()
print('Самое длинное слово:', max(string), '\nДлина слова "' + max(string) + '":', len(max(string)), 'символов')

# biggest_word = ''
# max_len = 0
# for word in string:
#     if len(word) > max_len:
#         max_len = len(word)
#         biggest_word = word
# print('Самое длинное слово:', biggest_word, '\nДлина слова "' + biggest_word + '":', max_len, 'символов')
