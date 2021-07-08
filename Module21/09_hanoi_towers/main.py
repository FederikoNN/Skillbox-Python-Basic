def move(n, x, y):
    if n == 1:
        print('Переложить диск 1 со стержня {} на стержень {}'.format(x, y))
        return
    else:
        move(n - 1, x, 6 - x - y)
        print('Переложить диск {} со стержня {} на стержень {}'.format(n, x, y))
        move(n - 1, 6 - x - y, y)


disc_num = int(input('Введите количество дисков: '))
move(disc_num, 1, 3)

# зачёт!
