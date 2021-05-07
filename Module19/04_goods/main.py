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
    good_available = store.get(goods.get(good))

    for i_good in good_available:
        goods_sum += i_good['quantity'] * i_good['price']
        goods_quantity += i_good['quantity']
    print(good, '-', goods_quantity, 'шт, стоимость', goods_sum, 'руб')

# зачёт!
