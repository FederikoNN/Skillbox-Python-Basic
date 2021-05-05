max_number = int(input('Введите максимальное число: '))
numbers_set = set(input('Нужное число есть среди вот этих чисел: ').split())
print('Ответ Артёма: Да')

while True:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers == 'Помогите!':
        break
    elif numbers_set.difference(set(numbers.split())):
        print('Ответ Артёма: Нет')
        numbers_set.difference_update(set(numbers.split()))
    elif len(numbers_set) == 1 and len(numbers.split()) == 1:
        print('Ответ Артёма: Вы угадали! Это число:', numbers)
        break
    else:
        print('Ответ Артёма: Да')

print('Артём мог загадать следующие числа:', ' '.join(sorted(numbers_set)))
