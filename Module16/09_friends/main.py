N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))
friends_balance = []
for _ in range(N):
    friends_balance.append(0)

for iou in range(K):
    print()
    print(iou + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_balance[to_whom - 1] -= how_much
    friends_balance[from_whom - 1] += how_much

print('\nБаланс друзей:')
for i_friends_balance in range(N):
    print(i_friends_balance + 1, ':', friends_balance[i_friends_balance])
