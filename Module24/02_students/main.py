import random


class Student:
    def __init__(self, name, group_num, achievements):
        self.name = name
        self.group_num = group_num
        self.achievements = achievements  # [score for score in achievements]


names = ['Светлана', 'Мария', 'Елена', 'Михаил', 'Олег', 'Тарас']
surname = ['Калиниченко', 'Шевченко', 'Пелых', 'Бондаренко', 'Скалолаз']
students_list = []
for _ in range(10):
    name = f'{random.choice(surname)} {random.choice(names)}'
    student = Student(name=name, group_num=random.randint(1, 3), achievements=[random.randint(2, 5) for _ in range(5)])
    students_list.append(student)

students_list.sort(key=lambda student: sum(student.achievements))
for student in students_list:
    print(f'{student.name} \tгруппа: {student.group_num} \tсредний балл: {sum(student.achievements) / 5}')
