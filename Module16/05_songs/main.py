violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input('Сколько песен выбрать? '))
total_time = 0
for song_number in range(N):
    print('\nНазвание', song_number + 1, 'песни: ', end='')
    song_name = input()
    for song in violator_songs:
        if song[0] == song_name:
            total_time += song[1]
            break

print('\n\nОбщее время звучания песен:', round(total_time, 2), 'минут')
