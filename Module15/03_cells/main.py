cells_list = [3, 0, 6, 2, 10]
wrong_cells_list = []
print('Кол-во клеток:', len(cells_list))

# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?

for i in range(len(cells_list)):
    print('Эффективность', i + 1, 'клетки:', cells_list[i])
    if i > cells_list[i]:
        wrong_cells_list.append(cells_list[i])

print('\nНеподходящие значения:', end='')
for cell in wrong_cells_list:
    print(cell, end=' ')
