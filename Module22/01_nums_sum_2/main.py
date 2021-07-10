file_in = open('numbers.txt', 'r')
data = [int(num) for num in file_in.read().split()]
file_in.close()
file_out = open('answer.txt', 'w')
file_out.write(str(sum(data)))
file_out.close()
