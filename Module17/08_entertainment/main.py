sticks_all = int(input('Кол-во палок: '))
cast = int(input('\nКол-во бросков: '))
sticks_answer = ['|' for _ in range(sticks_all)]
for i_cast in range(1, cast + 1):
    print('\nБросок', str(i_cast) + '.', end='')
    L_i = int(input('Сбиты палки с номера '))
    R_i = int(input('\nпо номер '))
    sticks_answer[L_i - 1: R_i] = ['.' for _ in range(L_i, R_i + 1)]
print(''.join(sticks_answer))

# зачёт!
