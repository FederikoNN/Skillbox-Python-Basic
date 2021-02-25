cells_list = [3, 0, 6, 2, 10]
wrong_cells_list = []
print('Кол-во клеток:', len(cells_list))

for cell_number in range(1, len(cells_list) + 1):
    print('Эффективность', cell_number, 'клетки:', cells_list[cell_number - 1])
    if cell_number > cells_list[cell_number - 1]:
        wrong_cells_list.append(cells_list[cell_number - 1])

print('\nНеподходящие значения:', end='')
for cell in wrong_cells_list:
    print(cell, end=' ')

# зачёт!
