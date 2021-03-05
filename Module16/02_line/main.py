rank_1 = list(range(160, 177, 2))
rank_2 = list(range(162, 181, 3))
rank_1.extend(rank_2)
rank_new = rank_1  # можно и не вводить новый список, а оставить rank_1

for i1_rank in range(len(rank_new) - 1):
    for i2_rank in range(i1_rank, len(rank_new)):
        if rank_new[i1_rank] > rank_new[i2_rank]:
            rank_new[i1_rank], rank_new[i2_rank] = rank_new[i2_rank], rank_new[i1_rank]
print('Отсортированный список', rank_new)
