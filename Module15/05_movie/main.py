films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_films = []
while True:
    choice_film = input('Введите любимый фильм (закончить ввод-0): ')
    flag = True
    if choice_film == '0':
        break
    for film in films:
        if choice_film == film:
            favorite_films.append(choice_film)
            flag = False
            break
    if flag:
        print('Фильм', '"' + choice_film + '"', '" отсутствует в списке!')
print('Список любимых фильмов:', favorite_films)
