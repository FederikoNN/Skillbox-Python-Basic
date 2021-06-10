list_old = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Вариант 1
# list_old = iter(list_old)
# list_new = [(i, y) for i, y in zip(list_old, list_old)]
# print(list_new)

# Вариант 2
# list_tmp_1 = [list_old[i] for i in range(0, len(list_old), 2)]
# list_tmp_2 = [list_old[i] for i in range(1, len(list_old), 2)]
# list_new = list(zip(list_tmp_1, list_tmp_2))
# print(list_new)

# Вариант 3
list_new = [tuple(list_old[i - 2:i]) for i in range(2, len(list_old) + 1, 2)]
print(list_new)

# зачёт!
