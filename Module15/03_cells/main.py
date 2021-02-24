cells_list = [3, 0, 6, 2, 10]
wrong_cells_list = []
print('Кол-во клеток:', len(cells_list))
for i in range(len(cells_list)):
    print('Эффективность', i + 1, 'клетки:', cells_list[i])
    if i > cells_list[i]:
        wrong_cells_list.append(cells_list[i])

print('\nНеподходящие значения:', end='')
for cell in wrong_cells_list:
    print(cell, end=' ')
