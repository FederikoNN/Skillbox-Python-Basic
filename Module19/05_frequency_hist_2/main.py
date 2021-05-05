def dict_invert(dictionary):
    dictionary_invert = dict()
    for i in dictionary.keys():
        if dictionary.get(i) in dictionary_invert.keys():
            a = list(dictionary_invert.get(dictionary.get(i)))
            a.append(i)
            dictionary_invert[dictionary.get(i)] = a
        else:
            dictionary_invert[dictionary.get(i)] = list(i)
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
