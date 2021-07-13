import random

summ = 0

with open('stat_log.txt', 'a') as file_stat:
    while summ < 777:
        try:
            num = int(input('Введите число: '))
            summ += num
            if random.randint(1, 13) == 13:
                raise BaseException
            file_stat.write(f'{num}\n')
        except BaseException:
            print('Выпало 13!')
            raise ValueError('Жаль! Но Вы не успели набрать 777 очков...')
    print('Игра окончена! Набрано 777 или более очков!')
