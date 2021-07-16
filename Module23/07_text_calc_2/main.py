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
            # file.write(string_new)
            return string_new
        elif choice == 'нет':
            return string
        else:
            print('Сделайте выбор! ', end='')


result = 0
with open('calc.txt', 'r') as file:
    print(f'Содержимое файла calc.txt:\n{file.read()}')
    file.seek(0)
    for line in file:
        line = line.strip(' \n')
        if not line.strip(' \n'):
            continue
        try:
            if len(line.split()) != 3:
                raise ValueError(f'Обнаружена ошибка')
            check_string(line)
        except (SyntaxError, TypeError, ValueError) as msg:
            print(msg)
            print(f'Обнаружена ошибка в строке: {line} Хотите исправить?', end=' ')
            line = correction(line)
        try:
            result += calc_text(line)
        except BaseException as msg:
            # print(msg)
            print('Очень жаль! Либо Вы не изменили строку, либо новая строка тоже некорректна! Идём дальше...')

print('Сумма результатов:', round(result, 2))
