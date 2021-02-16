def common_divisor_min(n):
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            print("Наименьший делитель, отличный от единицы:", divisor)
            break


number = int(input('Введите число: '))
common_divisor_min(number)

# зачёт!
