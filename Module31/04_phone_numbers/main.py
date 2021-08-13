import re

numbers = ['9999999999', '999999-999', '99999x9999']

pattern_num = r'[8|9]{1}\d{9}$'


def check_number(numbers_list: list, pattern: str) -> None:
    count = 1
    for num in numbers_list:
        if re.match(pattern, num):
            print(f'{count} номер: всё в порядке')
        else:
            print(f'{count} номер: не подходит')
        count += 1


check_number(numbers_list=numbers, pattern=pattern_num)
