def file_data_view(file):
    file_data = open(file)
    print('\nСодержимое файла {}:'.format(file))
    print(file_data.read())
    file_data.close()


file_in = open('numbers.txt', 'r')
file_data_view('numbers.txt')
data = [int(num) for num in file_in.read().split()]
file_in.close()
file_out = open('answer.txt', 'w')

file_out.write(f"{sum(data)}")
file_out.close()
file_data_view('answer.txt')
