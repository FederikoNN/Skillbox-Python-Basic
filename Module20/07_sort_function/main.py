def sort_tuple(tuple_ex):
    for i_tuple_ex in tuple_ex:
        if not isinstance(i_tuple_ex, int):
            return tuple_ex
    return sorted(tuple_ex)


tuple_old = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5)

print(sort_tuple(tuple_old))
