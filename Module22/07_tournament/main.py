def save_result_to_file(dict, file_name, score):
    dict_keys_list = list(dict.keys())
    dict_keys_list.sort(reverse=True)
    file_out = open(file_name, 'w')
    count = 0
    for key in dict_keys_list:
        if key > score:
            count += 1
            file_out.write('\n{}) {}'.format(str(count), dict[key]))
        else:
            file_out.seek(0)
            file_out.write(str(count))
            file_out.close()
            return
    file_out.close()
    return


def file_data_view(file):
    file_data = open(file)
    print('\nСодержимое файла {}:'.format(file))
    print(file_data.read())
    file_data.close()


file_data_view('first_tour.txt')
file_in = open('first_tour.txt')
K = int(file_in.readline())
players = {}
for line in file_in:
    str_tmp = line.split()
    players[int(str_tmp[2])] = (str_tmp[1])[0] + '. ' + str_tmp[0] + ' ' + str_tmp[2]

save_result_to_file(players, 'second_tour.txt', K)
file_data_view('second_tour.txt')
