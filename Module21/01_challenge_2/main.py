def print_number(num):
    if num == 0:
        return
    print_number(num - 1)
    print(num)


number = int(input('Введите число: '))
print_number(number)

# зачёт!
# зачёт!
