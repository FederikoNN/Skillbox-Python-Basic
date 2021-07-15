def except_for_string(string):
    string_list = string.split()
    string = ' '.join(string_list)
    if len(string_list) != 3:
        raise ValueError('Не хватает данных')
    if not string_list[0].isalpha():
        raise NameError('Ошибка в имени')
    if '@' not in string_list[1] or '.' not in string_list[1]:
        raise SyntaxError('Ошибка в E-mail')
    if not (string_list[2]).isdigit() or not 10 <= int(string_list[2]) < 99:
        raise ValueError('Ошибка в возрасте')
    return string + '\n'


with open('registrations.txt', 'r', encoding='utf-8') as file_in:
    with open('registrations_good.log', 'a') as file_good_data:
        with open('registrations_bad.log', 'a') as file_bad_data:
            for line in file_in:
                if not line.strip(' \n'):
                    continue
                string_out = line.strip(' \n')
                try:
                    string_out = except_for_string(line)
                except NameError as msg:
                    string_out += f'\t({msg})'
                except SyntaxError as msg:
                    string_out += f'\t({msg})'
                except ValueError as msg:
                    string_out += f'\t({msg})'
                if string_out == line:
                    file_good_data.write(line)
                else:
                    file_bad_data.write(f'{string_out}\n')
