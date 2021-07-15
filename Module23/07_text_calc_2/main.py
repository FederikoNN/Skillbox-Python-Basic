def check_string(string):
    operation = '+ - * / // %'
    string_list = string.split()
    if not string_list[0].isdigit() or not string_list[2].isdigit():
        raise TypeError('Ошибка в типе данных. Операнд(ы)- не целое число')
    if string_list[1] not in operation:
        raise SyntaxError('Ошибка в знаке операции')


def calc_text(string):
    list_in = string.split()
    x = int(list_in[0])
    y = int(list_in[2])
    oper = list_in[1]
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
with open('calc.txt', 'r') as file:
    print(f'Содержимое файла calc.txt:\n{file.read()}')
    file.seek(0)
    line_list = file.readlines()
    length = len(line_list)
    for line in line_list:
        line = line.strip(' \n')
        if not line.strip(' \n'):
            continue
        try:
            if len(line.split()) != 3:
                raise ValueError(f'Обнаружена ошибка')
            check_string(line)
            result += calc_text(line)
            list_tmp.append(line + '\n')
            print(list_tmp, length)
        except (SyntaxError, TypeError, ValueError) as msg:
            print(msg)
            print(f'Обнаружена ошибка в строке: {line} Хотите исправить?', end=' ')
            correction(line)
        # list_tmp.append(line + '\n')
with open('calc.txt', 'w') as file:
    print(''.join(list_tmp[:length]))
    file.write(''.join(list_tmp[:length]))

print('Сумма результатов:', round(result, 2))
