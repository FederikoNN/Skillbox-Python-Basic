N = int(input('Введите длину списка: '))
list_number = [1 if i_N % 2 == 0 else i_N % 5 for i_N in range(N)]
print('Результат:', list_number)

# зачёт!
