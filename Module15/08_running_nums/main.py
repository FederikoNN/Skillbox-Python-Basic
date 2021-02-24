list_old = [1, 2, 3, 4, 5]
list_new = [0, 0, 0, 0, 0]
K = int(input('Сдвиг: '))
for i in range(len(list_old)):
    list_new[(i + 1 + K) % len(list_old) - 1] = list_old[i]
print('Изначальный список:', list_old)
print('Сдвинутый список:', list_new)
