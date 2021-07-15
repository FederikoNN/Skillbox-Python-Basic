def check_string(string):
    operation = '+ - * / // %'
    string_list = string.split()
    if not string_list[0].isdigit() or not string_list[2].isdigit():
        raise TypeError('Ошибка в типе данных. Операнд(ы)- не целое число')
    if string_list[1] not in operation:
        raise SyntaxError('Ошибка в знаке операции')


def calc_text(list_in):
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
        raise SyntaxError('Ошибка в знаке операции')


result = 0
with open('calc.txt', 'r') as file:
    for line in file:
        try:
            line_list = line.split()
            if len(line_list) != 3:
                raise ValueError(f'Обнаружена ошибка')
            check_string(line)
            result += calc_text(line_list)
        except (SyntaxError, TypeError, ValueError) as msg:
            print(f'{msg} в строке: {line}')
print('Сумма результатов:', round(result, 2))

# зачёт!
