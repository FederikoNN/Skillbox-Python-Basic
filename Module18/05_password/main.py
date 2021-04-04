password = input('Придумайте пароль: ')

while True:
    if password.islower() or len(password) < 8:
        password = input('Пароль ненадёжный. Попробуйте ещё раз.\nПридумайте пароль: ')
    elif len(''.join(digit for digit in password if digit.isdigit())) < 3:
        password = input('Пароль ненадёжный. Попробуйте ещё раз.\nПридумайте пароль: ')
    else:
        print('Это надёжный пароль!')
        break

# зачёт!
