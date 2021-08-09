def simple_num(num):
    for i_num in range(2, num):
        if not num % i_num:
            return False
    return True


for number in range(2, 1001):
    if simple_num(number):
        print(number)

print([num for num in range(2, 1000) if not [i_num for i_num in range(2, num) if not num % i_num]])

simple_num_list = list(
    filter(lambda num: not [i_num for i_num in range(2, num) if not num % i_num != 0], range(2, 1000)))
print(simple_num_list)

simple_num_list = list(filter(lambda num: all(map(lambda i_num: num % i_num != 0, range(2, num))), range(2, 1000)))
print(simple_num_list)

# зачёт!
