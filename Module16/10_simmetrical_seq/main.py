def check_array(array):
    for i_array in range(len(array) // 2 + 1):
        if array[i_array] != array[len(array) - i_array - 1]:
            return 0
    return 1


N = int(input('Кол-во чисел: '))
numbers = []
numbers_add = []
for _ in range(N):
    numbers.append(int(input('Число: ')))
print('\nПоследовательность:', end=' ')
for number in numbers:
    print(number, end=' ')

i = 0
while check_array(numbers) == 0:
    numbers_add.insert(0, numbers[i])
    numbers.insert(N, numbers_add[0])
    i += 1
if numbers_add:
    print('\nНужно приписать чисел:', len(numbers_add))
    print('Сами числа:', end=' ')
    for number in numbers_add:
        print(number, end=' ')
else:
    print('\nПоследовательность симметричная')

# зачёт!
