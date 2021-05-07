family_tree = dict()
family_members = dict()
members_count = int(input('Введите количество человек: '))
for i_pair in range(1, members_count):
    print(i_pair, 'пара:', end=' ')
    pair = input().split()
    family_tree[pair[0]] = pair[1]

for member in family_tree.keys():
    count = 0
    tmp = member
    while True:
        if not family_tree.get(tmp):
            break
        tmp = family_tree.get(tmp)
        count += 1
    family_members[member] = count
member_0 = set(family_tree.values()) - set(family_tree.keys())
family_members[member_0.pop()] = 0

print('“Высота” каждого члена семьи:')
for member, height in sorted(family_members.items()):
    print(member, height)

# зачёт!
