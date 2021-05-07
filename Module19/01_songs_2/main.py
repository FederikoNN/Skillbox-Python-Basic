violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

N = int(input('Сколько песен выбрать? '))
total_time = 0
for i_song in range(1, N + 1):
    while True:
        print('\nНазвание', i_song, 'песни: ', end='')
        song_name = input()
        if song_name in violator_songs.keys():
            break
        else:
            print('Ошибка! Нет такой песни.')
    total_time += violator_songs.get(song_name)
print('\nОбщее время звучания песен:', round(total_time, 2), 'минут')

# зачёт!
