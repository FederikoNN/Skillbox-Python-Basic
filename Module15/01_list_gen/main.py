N = int(input('Введите число: '))
odd_numbers_list = []

# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" не отражает =)
for i in range(1, N + 1, 2):
    odd_numbers_list.append(i)
print(odd_numbers_list)
