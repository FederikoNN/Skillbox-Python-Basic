def except_for_string(string):
    string_list = string.split()
    string = ' '.join(string_list)
    try:
        if len(string_list) != 3:
            raise ValueError('Не хватает данных')
        try:
            if not string_list[0].isalpha():
                raise NameError('Ошибка в имени')
        except NameError as e:
            string += f'\t({e})'
        try:
            if '@' not in string_list[1] or '.' not in string_list[1]:
                raise SyntaxError('Ошибка в E-mail')
        except SyntaxError as e:
            string += f'\t({e})'
        try:
            if not (string_list[2]).isdigit() or not 10 <= int(string_list[2]) < 99:
                raise ValueError('Ошибка в возрасте')
        except ValueError as e:
            string += f'\t({e})'
    except ValueError as e:
        string += f'\t({e})'
    return string + '\n'


with open('registrations.txt', 'r', encoding='utf-8') as file_in:
    with open('registrations_good.log', 'a') as file_good_data:
        with open('registrations_bad.log', 'a') as file_bad_data:
            for line in file_in:
                if not line.strip(' \n'):
                    continue
                string_out = except_for_string(line)
                if string_out == line:
                    file_good_data.write(line)
                else:
                    file_bad_data.write(f'{string_out}')
