data_1 = [1, 3, 4, 5]
data_2 = 'sdhsdfhsfhss'
print('Данные № 1:', data_1)
print('Данные № 2:', data_2)
print('\nРезультат:')


def zip_alter(array_1, array_2):
    return ((array_1[i], array_2[i]) for i in range(min(len(array_1), len(array_2))))


print(zip_alter(data_1, data_2))
for i_tuple in zip_alter(data_1, data_2):
    print(i_tuple)

# зачёт!
