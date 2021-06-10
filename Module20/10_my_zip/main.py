string = 'abcdaaa'
numbers_tuple = (10, 20, 30, 40)
print('Строка:', string)
print('Кортеж чисел:', numbers_tuple)
print('\nРезультат:')
tuple_generator = zip(string, numbers_tuple)
print(tuple_generator)
for i_tuple in tuple_generator:
    print(i_tuple)


def zip_alter(array_1, array_2):
    return ((array_1[i], array_2[i]) for i in range(min(len(array_1), len(array_2))))


print(zip_alter(string, numbers_tuple))
for i_tuple in zip_alter(string, numbers_tuple):
    print(i_tuple)

# зачёт!
