file = open('zen.txt', 'r')
zen_in = file.readlines()
print(zen_in[len(zen_in) - 1])
for line in reversed(zen_in[:-1]):
    print(line, end='')
file.close()
