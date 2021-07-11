file_in = open('numbers.txt', 'r')
data = [int(num) for num in file_in.read().split()]
file_in.close()
file_out = open('answer.txt', 'w')

# TODO, предлагаю производить запись в файл без использования str.
#  В таком случае, стоит использовать форматирование строк.
#  Возможно, Вам тоже покажется удобным форматирование при помощи f-строк.
#  https://python-scripts.com/f-strings
file_out.write(str(sum(data)))
file_out.close()

# TODO, пожалуйста, добавьте вывод содержимого файла.