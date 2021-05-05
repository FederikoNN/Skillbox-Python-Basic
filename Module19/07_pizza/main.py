N_orders = int(input('Введите кол-во заказов: '))
orders_DB = dict()
for i_order in range(1, N_orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input().split()
    if order[0] not in orders_DB:
        orders_DB[order[0]] = {order[1]: order[2]}
    elif order[1] in orders_DB.get(order[0]):
        orders_DB.get(order[0])[order[1]] = int(orders_DB.get(order[0], {}).get(order[1])) + int(order[2])
    else:
        orders_DB.get(order[0])[order[1]] = order[2]

for family, orders_list in sorted(orders_DB.items()):
    print(family + ':')
    for pizza, quantity in sorted(orders_list.items()):
        print('\t', pizza + ':', quantity)
