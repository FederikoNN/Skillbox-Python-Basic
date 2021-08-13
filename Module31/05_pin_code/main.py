import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
brute_force = itertools.product(digits, repeat=4)
count = 1
for combination in brute_force:
    print(f'{count} вариант: {combination}')
    count += 1
