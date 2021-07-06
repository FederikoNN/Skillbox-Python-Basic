def fibonachi(num):
    pos = 1
    if num > 2:
        pos = fibonachi(num - 1) + fibonachi(num - 2)
    return pos


pos_number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonachi(pos_number))
