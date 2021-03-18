vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
text = input('Введите текст: ')
vowels_list = [sym for sym in text if sym in vowels]
print('Список гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))

# зачёт!
