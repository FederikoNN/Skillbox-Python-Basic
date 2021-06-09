entry_number = int(input('Сколько записей вносится в протокол? '))
protocol = []
for number in range(1, entry_number + 1):
    print(number, 'запись:', end=' ')
    entry = input().split()
    # TODO, предлагаю упростить решение и решить без использования методов remove, extend, pop и index.
    #  По итогам цикла стоит попробовать получить словарь где Ключи это имена участников, а значения списки
    #  c [Максимальный счёт, Номер записи].
    # TODO, можно попробовать реализовать сортировку при помощи функции lambda.
    #  Давайте попробуем https://pythoner.name/sortdict.

    if entry[1] in protocol and int(entry[0]) > int(protocol[protocol.index(entry[1]) - 1]):
        protocol.pop(protocol.index(entry[1]) - 1)
        protocol.remove(entry[1])
        protocol.extend(entry)
    elif entry[1] in protocol and int(entry[0]) <= int(protocol[protocol.index(entry[1]) - 1]):
        continue
    else:
        protocol.extend(entry)

protocol = iter(protocol)
protocol_new = [(int(i), y) for i, y in zip(protocol, protocol)]

print('\nИтоги соревнований:')

for i in range(1, 4):
    max_score = 0
    max_name = ''
    for score, name in protocol_new:
        if score > max_score:
            max_score = score
            max_name = name
    print(i, 'место.', max_name, '(' + str(max_score) + ')')
    protocol_new.remove((max_score, max_name))
