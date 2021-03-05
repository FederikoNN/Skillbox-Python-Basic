rank_1 = list(range(160, 177, 2))
rank_2 = list(range(162, 181, 3))
rank_1.extend(rank_2)
rank_new = rank_1  # можно и не вводить новый список, а оставить rank_1
rank_new.sort()  # TODO как решить без sort? =)
print('Отсортированный список', rank_new)
