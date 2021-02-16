def search_digit(x):
    digit_4 = str(x % 10)
    digit_3 = str((x // 10) % 10)
    digit_2 = str(((x // 10) // 10) % 10)
    digit_1 = str(x // 1000)
    count = 0
    for digit in str(x):
        if digit_4 == digit:
            count += 1
    if count == 3:
        print(x)
    elif count == 1 and digit_1 == digit_2 == digit_3:
        print(x)


year_first = int(input('Введите первый год: '))
year_second = int(input('Введите второй год: '))
print('\nГоды от', year_first, 'до', year_second, 'с тремя одинаковыми цифрами:')
for year in range(year_first, year_second + 1):
    search_digit(year)

# зачёт!
