def sort_tuple(tuple_ex):
    if not ''.join(str(i) for i in tuple_ex).isdigit():
        return tuple_ex
    else:
        return tuple(sorted(list(tuple_ex)))


tuple_old = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 'a')

print(sort_tuple(tuple_old))
