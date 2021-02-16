def common_divisor_min(n):
    for x in range(2, n + 1):
        if n % x == 0:
            print("Наименьший делитель, отличный от единицы:", x)
            break


n = int(input('Введите число: '))
common_divisor_min(n)
