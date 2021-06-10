entry_number = int(input('Сколько записей вносится в протокол? '))
protocol = {}
for number in range(1, entry_number + 1):
    print(number, 'запись:', end=' ')
    entry = input().split()
    if entry[1] in protocol.keys() and int(entry[0]) <= protocol.get(entry[1])[0]:
        continue
    else:
        protocol[entry[1]] = [int(entry[0]), number]

list_protocol = list(protocol.items())
list_protocol.sort(key=lambda i: i[1][1])
list_protocol.sort(key=lambda i: i[1][0], reverse=True)

print('\nИтоги соревнований:')
for i_list_protocol in range(3):
    print(i_list_protocol + 1, 'место.', list_protocol[i_list_protocol][0],
          '(' + str(list_protocol[i_list_protocol][1][0]) + ')')
