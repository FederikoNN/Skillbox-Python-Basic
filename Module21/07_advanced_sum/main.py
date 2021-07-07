def sum_advance(*args):
    summ = 0
    for i_args in args:
        if isinstance(i_args, list):
            for i_args_list in i_args:
                summ += sum_advance(i_args_list)
        else:
            summ += i_args
    return summ


example = sum_advance([[1, 2, [3]], [1], 3], 1, 2, 3, 4, 5)
print('Ответ:', example)
