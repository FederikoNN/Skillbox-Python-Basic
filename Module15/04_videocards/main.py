video_cards_list = [3070, 2060, 3090, 3070, 3090]
video_cards_list_new = []

print('Кол-во видеокарт:', len(video_cards_list))
for list_index in range(1, len(video_cards_list) + 1):
    print(list_index, 'Видеокарта:', video_cards_list[list_index - 1])
    for card in video_cards_list:
        if video_cards_list[list_index - 1] < card:
            video_cards_list_new.append(video_cards_list[list_index - 1])
            break
print('\nСтарый список видеокарт:', video_cards_list)
print('Новый список видеокарт:', video_cards_list_new)

# зачёт!
