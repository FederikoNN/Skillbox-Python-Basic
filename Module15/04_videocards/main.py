video_cards_list = [3070, 2060, 3090, 3070, 3090]
video_cards_list_new = []
# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
print('Кол-во видеокарт:', len(video_cards_list))
for i in range(len(video_cards_list)):
    print(i + 1, 'Видеокарта:', video_cards_list[i])
    for card in video_cards_list:
        if video_cards_list[i] < card:
            video_cards_list_new.append(video_cards_list[i])
            break
print('\nСтарый список видеокарт:', video_cards_list)
print('Новый список видеокарт:', video_cards_list_new)
