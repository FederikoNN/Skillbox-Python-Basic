file_in = open('numbers.txt', 'r')
print('\nСодержимое файла {}:'.format('numbers.txt'))
print(file_in.read())
data = [int(num) for num in file_in.read().split()]
file_in.close()
file_out = open('answer.txt', 'w+')

file_out.write(f"{sum(data)}")
file_out.seek(0)
print('Содержимое файла {}:'.format('answer.txt'))
print(file_out.read())
file_out.close()
