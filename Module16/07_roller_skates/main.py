def difference_min(num, array):
    min_diff = num
    for content in array:
        if content - num < min_diff and num <= content:
            min_diff = content - num
    if min_diff != num:
        array.remove(min_diff + num)
    return min_diff


count_persons = 0
rollers = []
rollers_quantity = int(input('Кол-во коньков: '))
# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
for rollers_num in range(rollers_quantity):
    print('Размер', rollers_num + 1, 'пары ', end='')
    rollers.append(int(input()))
rollers.sort()

people_num = int(input('\nКол-во людей: '))
# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
for person in range(people_num):
    print('Размер ноги', person + 1, 'человека: ', end='')
    foot_size = int(input())
    if foot_size != difference_min(foot_size, rollers):
        count_persons += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_persons)

