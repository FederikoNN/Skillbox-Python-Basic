def list_create(num, array):
    for i_num in range(num):
        print('Введите', i_num + 1, 'число: ', end='')
        array.append(int(input()))


list_1 = []
list_2 = []

print('Первый список\n')
list_create(3, list_1)
print('\nВторой список\n')
list_create(7, list_2)
print('\nПервый список:', list_1)
print('\nВторой список:', list_2, '\n')

list_1.extend(list_2)
for number in list_1:
    for _ in range(list_1.count(number) - 1):
        list_1.remove(number)

print('\nНовый первый список с уникальными элементами:', list_1)

# зачёт!
