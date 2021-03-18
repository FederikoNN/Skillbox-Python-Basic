nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

answer = [num for nice_list_sub_01 in nice_list for nice_list_sub_02 in nice_list_sub_01 for num in nice_list_sub_02]
print(answer)
