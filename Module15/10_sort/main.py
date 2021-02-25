list_num = [1, 4, -3, 0, 10, -127, 15]
N = len(list_num)
tmp = 0

print('Изначальный список:', list_num)
for _ in range(N - 1):
    for list_index in range(N - 1):
        if list_num[list_index] > list_num[list_index + 1]:
            tmp = list_num[list_index + 1]
            list_num[list_index + 1] = list_num[list_index]
            list_num[list_index] = tmp
print('Отсортированный список:', list_num)
