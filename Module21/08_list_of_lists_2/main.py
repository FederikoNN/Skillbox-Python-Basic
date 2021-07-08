nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# def list_extern(list_in):
#     list_ext = []
#     for i_list in list_in:
#
#         if isinstance(i_list, list):
#             list_ext.extend(list_extern(i_list))
#         else:
#             list_ext.append(i_list)
#
#     return list_ext

def list_extern(list_in):
    if not list_in:
        return list_in
    elif isinstance(list_in[0], list):
        return list_extern(list_in[0]) + list_extern(list_in[1:])
    else:
        return list_in[:1] + list_extern(list_in[1:])


print('Ответ:', list_extern(nice_list))
