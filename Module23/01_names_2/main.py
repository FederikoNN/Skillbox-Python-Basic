sym_num = 0
line_count = 0
with open('people.txt', 'r') as file_in:
    for line in file_in:
        length = len(line)
        line_count += 1
        if line.endswith('\n'):
            length -= 1
        try:
            if length < 3:
                raise BaseException
        except BaseException:
            msg = 'Ошибка! Длина {} строки меньше 3 символов!'.format(line_count)
            print(msg)
            with open('errors.log', 'a') as file_out:
                file_out.write(msg + '\n')
        sym_num += length
print('Общая сумма символов:', sym_num)

# зачёт!
# зачёт!
