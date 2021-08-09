import collections


def can_be_poly(string):
    sym_dict = dict(collections.Counter(string))
    if len(list(filter(lambda sym: sym_dict[sym] % 2, sym_dict))) > 1:
        return False
    return True


print(can_be_poly('ababc'))
print(can_be_poly('abbcb'))

# зачёт!
