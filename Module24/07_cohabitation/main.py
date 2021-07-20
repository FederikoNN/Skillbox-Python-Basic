import random


class Human:
    def __init__(self, name, home, satiety=50):
        self.name = name
        self.satiety = satiety
        self.home = home

    def get_name(self):
        return self.name

    def eat(self):
        print(f'{self.name} покушал')
        if self.satiety >= 0:
            self.satiety += 1
            self.home.food -= 1

    def work(self):
        print(f'{self.name} работает')
        self.satiety -= 1
        self.home.money += 1

    def play(self):
        print(f'{self.name} решил поиграть')
        if self.satiety > 0:
            self.satiety -= 1

    def food_shopping(self):
        if self.home.money > 0:
            print(f'{self.name} сходил в магазин за продуктами')
            self.home.money -= 1
            self.home.food += 1

    def is_alive(self):
        if self.satiety < 0:
            print(f'{self.name} не выдержал таких нагрузок...')
            return False
        return True

    def one_day_of_life(self):
        cube_gen = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.food < 10:
            self.food_shopping()
        elif self.home.money < 50:
            self.work()
        elif cube_gen == 1:
            self.work()
        else:
            self.play()
        self.print_info()

    def print_info(self):
        print(f'{self.name} сытость: {self.satiety}')


class Home:
    def __init__(self, resident=None, food=50, money=0):
        self.residents = []
        self.food = food
        self.money = money
        self.add_resident(resident)

    def add_resident(self, human):
        if isinstance(human, Human):
            self.residents.append(human)

    def life_flow(self):
        for i_resident in self.residents:
            i_resident.one_day_of_life()
        self.print_info()

    def print_info(self):
        print(f'Еда в доме: {self.food}; деньги в доме: {self.money}\n')


home = Home()
human_01 = Human('Николай', home)
human_02 = Human('Пётр', home)
home.add_resident(human_01)
home.add_resident(human_02)

for day in range(1, 366):
    print(f'День {day}:')
    if not human_01.is_alive() or not human_02.is_alive():
        break
    home.life_flow()

# зачёт!
