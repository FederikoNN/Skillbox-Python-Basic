N = int(input('Кол-во стран: '))
country_dict = {}

for i_country in range(1, N + 1):
    print(i_country, 'страна: ', end='')
    tmp_list = input().split()
    country_dict[tmp_list[0]] = tmp_list[1:]

for count in range(1, 4):
    print(count, 'город:', end=' ')
    city = input()
    for country in country_dict.keys():
        if city in country_dict.get(country):
            print('Город', city, 'расположен в стране', country, end='.\n')
            break
        elif country == list(country_dict.keys())[-1]:
            print('По городу', city, 'данных нет.')

# зачёт!
