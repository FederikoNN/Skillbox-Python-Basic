N_orders = int(input('Введите кол-во заказов: '))
orders_DB = dict()
for i_order in range(1, N_orders + 1):
    print(i_order, 'заказ: ', end='')
    order = input().split()
    client = order[0]
    pizza = order[1]
    quantity = order[2]
    if client not in orders_DB:
        orders_DB[client] = {pizza: quantity}
    elif pizza in orders_DB.get(client):
        orders_DB.get(client)[pizza] = int(orders_DB.get(client, {}).get(pizza)) + int(quantity)
    else:
        orders_DB.get(client)[pizza] = quantity

for family, orders_list in sorted(orders_DB.items()):
    print(family + ':')
    for pizza, quantity in sorted(orders_list.items()):
        print('\t', pizza + ':', quantity)
