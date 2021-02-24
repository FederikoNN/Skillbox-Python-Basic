list_num = [1, 4, -3, 0, 10]
N = len(list_num)
tmp = 0
print('Изначальный список:', list_num)
for _ in range(N - 1):
    for i in range(N - 1):
        if list_num[i] > list_num[i + 1]:
            tmp = list_num[i + 1]
            list_num[i + 1] = list_num[i]
            list_num[i] = tmp
print('Отсортированный список:', list_num)
