def synonym_search(syn_dict, word_in):
    for key, value in syn_dict.items():
        if key.lower() == word_in:
            print('Синоним:', value)
            return True
        elif value.lower() == word_in:
            print('Синоним:', key)
            return True
    return False


N_pairs = int(input('Введите количество пар слов: '))
synonym_dict = dict()
for i_pair in range(1, N_pairs + 1):
    print(i_pair, 'пара:', end=' ')
    words_pair = input().split()
    synonym_dict[words_pair[0]] = words_pair[2]
print()
while True:
    word = input('Введите слово: ').lower()
    if synonym_search(synonym_dict, word):
        break
    print('Такого слова в словаре нет.')

# зачёт!
