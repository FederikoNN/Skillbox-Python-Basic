file = open('zen.txt', 'r')
zen_in = file.readlines()


# TODO, предлагаю упростить решение и просто применить обратный срез к переменной zen_in.
#  В таком случае, использование функции reversed будет лишним. =)
print(zen_in[len(zen_in) - 1])
for line in reversed(zen_in[:-1]):
    print(line, end='')
file.close()
