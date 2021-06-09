students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

for id_student, student in students.items():
    print(id_student, student.get('age'))


def total_data(student_order):
    interest_order = []
    surnames_length = 0
    for _, student in student_order.items():
        interest_order.extend(student.get('interests'))
        surnames_length += len(student.get('surname'))
    return interest_order, surnames_length


interests_list, total_length = total_data(students)
print(interests_list, total_length)

# зачёт!
