guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    guest_go = input('Гость пришёл или ушёл? ')
    if guest_go == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    guest_name = input('Имя гостя: ')
    if guest_name == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

    if guest_go == 'пришёл' and len(guests) == 6:
        print('Прости,', guest_name + ', но мест нет.')
    elif guest_go == 'ушёл' and len(guests) <= 6:
        print('Пока,', guest_name + '!')
        guests.remove(guest_name)
    else:
        print('Привет,', guest_name + '!')
        guests.append(guest_name)
