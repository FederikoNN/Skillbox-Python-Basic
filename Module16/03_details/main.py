shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

choice = input('Название детали: ')
count = 0
cost = 0
for item in shop:
    count += item.count(choice)
    if item[0] == choice:
        cost += item[1]
print('\n\nКол-во деталей -', count)
print('Общая стоимость -', cost)

# зачёт!
