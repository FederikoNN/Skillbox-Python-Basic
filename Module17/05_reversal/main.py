string = input('Введите строку: ')

string_changed = string[:string.index('h')] + string[len(string) - string[::-1].index(
    'h') - 1:string.index('h'):-1] + string[len(string) - string[::-1].index('h') - 1:]

print('\nРезультат:', string_changed)
