def calc_text(list_in):
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
            raise SyntaxError('Ошибка в знаке операции')
    else:
        raise TypeError('Ошибка в типе данных. Операнд(ы)- не целое число')


result = 0
with open('calc.txt', 'r') as file:
    for line in file:
        try:
            line_list = line.split()
            if len(line_list) != 3:
                raise ValueError(f'Обнаружена ошибка в строке {line}')
            result += calc_text(line_list)
        except ValueError as msg:
            print(msg)
        except SyntaxError as msg:
            print(f'{msg} в строке: {line}')
        except TypeError as msg:
            print(f'{msg} в строке: {line}')
print('Сумма результатов:', round(result, 2))
