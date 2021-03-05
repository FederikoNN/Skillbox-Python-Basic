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

for rollers_num in range(1, rollers_quantity + 1):
    print('Размер', rollers_num, 'пары ', end='')
    rollers.append(int(input()))
rollers.sort()

people_num = int(input('\nКол-во людей: '))

for person in range(1, people_num + 1):
    print('Размер ноги', person, 'человека: ', end='')
    foot_size = int(input())
    if foot_size != difference_min(foot_size, rollers):
        count_persons += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_persons)
