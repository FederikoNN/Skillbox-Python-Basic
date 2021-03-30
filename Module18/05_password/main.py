password = input('Придумайте пароль: ')

while password.islower() or len(password) < 8 or len(
        ''.join(digit for digit in password if digit.isdigit())) < 3:
    password = input('Пароль ненадёжный. Попробуйте ещё раз.\nПридумайте пароль: ')

print('Это надёжный пароль!')
