def dict_invert(dictionary):
    dictionary_invert = dict()
    for key in dictionary.keys():
        if dictionary.get(key) in dictionary_invert.keys():
            a = list(dictionary_invert.get(dictionary.get(key)))
            a.append(key)
            dictionary_invert[dictionary.get(key)] = a
        else:
            dictionary_invert[dictionary.get(key)] = list(key)
    return dictionary_invert


text = input('Введите текст: ')
hist = dict()
for sym in text:
    if sym in hist:
        hist[sym] += 1
    else:
        hist[sym] = 1

print('Оригинальный словарь частот:')
for key, value in sorted(hist.items()):
    print(key, ':', value)

print('\nИнвертированный словарь частот:')
for key, value in dict_invert(hist).items():
    print(key, ':', value)

# зачёт!
