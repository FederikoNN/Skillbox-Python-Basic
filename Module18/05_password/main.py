password = input('Придумайте пароль: ')



# TODO, Не очень хорошо делать такие большие условие в условии цикла while.
#  Предлагаю попробовать реализовать циклом while True с проверками внутри.
#  Цель, сделать код более читаемым =)
while password.islower() or len(password) < 8 or len(
        ''.join(digit for digit in password if digit.isdigit())) < 3:
    password = input('Пароль ненадёжный. Попробуйте ещё раз.\nПридумайте пароль: ')

print('Это надёжный пароль!')

