N = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, 'человек')
people = list(range(1, N + 1))
count_point = 0
while len(people) > 1:
    print('\nТекущий круг людей:', people)
    print('Начало счёта с номера', people[count_point % len(people)])
    count_point = (count_point + K - 1) % len(people)
    people.remove(people[count_point])
print('Остался человек под номером', people[0])

# зачёт!
