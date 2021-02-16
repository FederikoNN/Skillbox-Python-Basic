def reverse_number(x):
    rev_num = ''
    while x != 0:
        rev_num += str(x % 10)
        x = x // 10
    return rev_num


def reverse_number_float(x):
    rev_num = reverse_number(int(x))
    x_fractional = ''
    for sym in reversed(str(x)):
        if sym == '.':
            break
        x_fractional += sym
    rev_num = rev_num + '.' + x_fractional
    return float(rev_num)


N = float(input('Введите первое число: '))
K = float(input('Введите второе число: '))
K_rev = reverse_number_float(K)
N_rev = reverse_number_float(N)
print('\nПервое число наоборот:', N_rev)
print('Второе число наоборот:', K_rev)
sum_rev = K_rev + N_rev
print('Сумма:', sum_rev)

# зачёт!
