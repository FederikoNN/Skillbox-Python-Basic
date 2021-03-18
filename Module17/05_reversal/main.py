string = input('Введите строку: ')

print('\nРезультат:', string[len(string) - string[::-1].index('h') - 2:string.index('h'):-1])
