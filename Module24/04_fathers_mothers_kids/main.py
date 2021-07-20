class Parent:
    def __init__(self, name, age=16, child_list=[]):
        self.age = age
        self.name = name
        self.child_list = []
        self.child = Child(name)
        self.add_child(child_list)

    def add_child(self, child_new):
        for child in child_new:
            if isinstance(child, Child) and self.age - child.age > 16:
                self.child_list.append(child)

    def get_parent_info(self):
        parent_info = {'Имя': self.name, 'Возраст': self.age,
                       'Дети': ', '.join([self.child.name for self.child in self.child_list])}
        for key, value in parent_info.items():
            print(f'{key}: {value}')

    def feed_child(self):
        print('\nПора покормить ребенка')
        self.child.eat()

    def calm_child(self):
        print('\nНадо успокоить ребенка')
        self.child.calm()

    def feed_all(self):
        print('\nНадо покормить детей')
        for i_child in self.child_list:
            i_child.eat()

    def calm_all(self):
        print('\nНадо успокоить детей')
        for i_child in self.child_list:
            i_child.calm()


class Child:
    calm_states = {0: 'Спокоен', 1: 'Слегка расстроен', 2: 'Возбужден'}
    hungry_states = {0: 'Очень голоден', 1: 'Ещё голоден', 2: 'Сыт и доволен'}

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.hungry_state = 0
        self.calm_state = 2

    def is_hungry(self):
        if self.hungry_state != 2:
            return True
        return False

    def is_calm(self):
        if self.calm_state == 2:
            return True
        return False

    def eat(self):
        self.print_state()
        if self.hungry_state < 2:
            print(f'{self.name}: Я поел')
            self.hungry_state += 1
        self.print_state()

    def calm(self):
        self.print_state()
        if self.calm_state != 0:
            print(f'{self.name}: Порадовали')
            self.calm_state -= 1
        self.print_state()

    def print_state(self):
        print(
            f'Ребенок {self.name} сейчас {Child.hungry_states[self.hungry_state]} и {Child.calm_states[self.calm_state]}')


child_01 = Child('Николай', 5)
child_02 = Child('Петр', 17)
parent = Parent('Владимир', 25, [child_01, child_02])
# parent.add_child([child_01, child_02])
parent.get_parent_info()

for _ in range(2):
    parent.feed_all()
    parent.calm_all()

# зачёт!
