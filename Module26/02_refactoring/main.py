list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

result = (f'\nНайдено: {x} x {y} = {to_find}' for x in list_1 for y in list_2 if x * y == to_find)
for i in result:
    print(i)


# TODO, пожалуйста, обратите внимание, в текущем решении не хватает ряда выводов, которые присутствовали в изначальном.
#  Стоит реализовать решением функцией-генератором =)

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break
