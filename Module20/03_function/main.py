def new_tuple_function(tuple, data):
    if tuple.count(data) == 0:
        new_tuple = ()  # Переменная получилась лишней, можно сразу вернуть ()
        return new_tuple
    elif tuple.count(data) == 1:
        return tuple[tuple.index(data):]
    elif tuple.count(data) >= 2:
        tmp = tuple[tuple.index(data) + 1:].index(data) + 2 + tuple.index(data)
        return tuple[tuple.index(data):tmp]


# text = input('Введите что-нибудь: ')
# tuple_old = tuple([sym for sym in text])
tuple_old = ("1", "2", "3", "4", "2", "5", "6")
element = input('Введите элемент: ')
print(new_tuple_function(tuple_old, element))

# зачёт!
