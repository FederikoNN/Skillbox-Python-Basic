def palindrome_check(text):
    stop_count = 0
    for sym in set(text):
        if text.count(sym) % 2 == 1:
            if stop_count == 1:
                print('Нельзя сделать палиндромом')
                return False
            stop_count += 1
    return True


string = ''.join(input('Введите строку: ').lower().split())

if palindrome_check(string):
    print('Можно сделать палиндромом')

# зачёт!
