file_in = open('numbers.txt', 'r')
print('\nСодержимое файла {}:'.format('numbers.txt'))
print(file_in.read())
file_in.seek(0)
data = [int(num) for num in file_in.read().split()]
file_in.close()
file_out = open('answer.txt', 'w+')

file_out.write(f"{sum(data)}")
file_out.seek(0)
print('Содержимое файла {}:'.format('answer.txt'))
print(file_out.read())
file_out.close()

# Альтернативный вариант кода без list сomprehension:
#
# summ = 0
# file_in = open('numbers.txt', 'r')
# print('\nСодержимое файла {}:'.format('numbers.txt'))
# print(file_in.read())
# file_in.seek(0)
# for num in file_in.read().split():
#     if num.isdigit():
#         summ += int(num)
# file_in.close()
# file_out = open('answer.txt', 'w+')
#
# file_out.write(f"{summ}")
# file_out.seek(0)
# print('Содержимое файла {}:'.format('answer.txt'))
# print(file_out.read())
# file_out.close()

# зачёт!
