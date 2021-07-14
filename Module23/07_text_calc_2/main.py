def calc_text(string):
    list_in = string.split()
    if len(list_in) != 3:
        raise ValueError('Ошибка в количестве аргументов.')
    x = list_in[0]
    y = list_in[2]
    oper = list_in[1]
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if oper == '+':
            return x + y
        elif oper == '-':
            return x - y
        elif oper == '*':
            return x * y
        elif oper == '/':
            return x / y
        elif oper == '//':
            return x // y
        elif oper == '%':
            return x % y
        else:
            raise SyntaxError('Ошибка в знаке операции.')
    else:
        raise TypeError('Ошибка в типе данных. Операнд(ы)- не целое число.')


def correction(string):
    while True:
        choice = input().lower()
        if choice == 'да':
            string_new = input('Введите исправленную строку: ')
            line_list.append(string_new)
            list_tmp.append(string_new + '\n')
            return
        elif choice == 'нет':
            list_tmp.append(string + '\n')
            return
        else:
            print('Сделайте выбор! ', end='')


result = 0
list_tmp = []
with open('calc.txt', 'r+') as file:
    print(f'Содержимое файла calc.txt:\n{file.read()}')
    file.seek(0)
    line_list = file.readlines()
    length = len(line_list)
    for line in line_list:
        line = line.strip(' \n')
        if not line.strip(' \n'):
            continue
        try:
            result += calc_text(line)
            list_tmp.append(line + '\n')
        except (SyntaxError, TypeError, ValueError) as msg:
            print(msg)
            print(f'Обнаружена ошибка в строке: {line} Хотите исправить?', end=' ')
            correction(line)
    file.seek(0)
    file.write(''.join(list_tmp[:length]))

print('Сумма результатов:', round(result, 2))
