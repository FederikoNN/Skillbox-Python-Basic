list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


# result = (f'\nНайдено: {x} x {y} = {to_find}' for x in list_1 for y in list_2 if x * y == to_find)
# for i in result:
#     print(i)

def find(list_01, list_02, num):
    for x in list_01:
        for y in list_02:
            yield f'{x} x {y} = {x * y}'
            if x * y == to_find:
                print('Found!!!')
                return
    print('Not found!!!')


a = find(list_1, list_2, to_find)
for i in a:
    print(i)
