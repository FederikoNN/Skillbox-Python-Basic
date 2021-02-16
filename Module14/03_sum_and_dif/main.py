def sum_digit(N):
    summ = 0
    while N != 0:
        summ += N % 10
        N = N // 10
    return summ


def quantity_digit(N):
    count = 0
    while N != 0:
        count += 1
        N = N // 10
    return count


N = int(input('Введите число: '))
print('\nСумма цифр:', sum_digit(N))
print('Количество цифр в числе:', quantity_digit(N))
print('Разность суммы и количества цифр:', sum_digit(N) - quantity_digit(N))
