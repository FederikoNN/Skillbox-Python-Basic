goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good in goods.keys():
    goods_sum = 0
    goods_quantity = 0

    # TODO, предлагаю попробовать сократить количество вычислений в коде.
    #  К примеру, создать переменную равную tore.get(goods.get(good))
    #  И далее в коде работать с ней.

    for i_goods in range(len(store.get(goods.get(good)))):
        goods_sum += (store.get(goods.get(good))[i_goods])['quantity'] * (store.get(goods.get(good))[i_goods])['price']
        goods_quantity += store.get(goods.get(good))[i_goods]['quantity']
    print(good, '-', goods_quantity, 'шт, стоимость', goods_sum, 'руб')
