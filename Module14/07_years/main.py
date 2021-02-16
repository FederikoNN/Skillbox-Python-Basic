def search_digit(x):
    a = str(x % 10)
    b = str((x // 10) % 10)
    c = str(((x // 10) // 10) % 10)
    d = str(x // 1000)
    count = 0
    for n in str(x):
        if a == n:
            count += 1
    if count == 3:
        print(x)
    elif count == 1 and b == c == d:
        print(x)


year_first = int(input('Введите первый год: '))
year_second = int(input('Введите второй год: '))
print('\nГоды от', year_first, 'до', year_second, 'с тремя одинаковыми цифрами:')
for year in range(year_first, year_second + 1):
    search_digit(year)
