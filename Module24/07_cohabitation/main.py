import random


class Human:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def get_name(self):
        return self.name

    def eat(self):
        print(f'{self.name} покушал')
        if self.satiety >= 0:
            self.satiety += 1

    def work(self):
        print(f'{self.name} работает')
        if self.satiety > 0:
            self.satiety -= 1

    def play(self):
        print(f'{self.name} решил поиграть')
        if self.satiety > 0:
            self.satiety -= 1

    def food_shopping(self):
        print(f'{self.name} сходил в магазин за продуктами')

    def is_alive(self):
        if self.satiety < 0:
            print(f'{self.name} не выдержал таких нагрузок...')
            return False
        return True

    def print_info(self):
        print(f'{self.name} сытость: {self.satiety}')


class Home:
    def __init__(self, residents=[], food=50, money=0):
        self.residents = residents
        self.food = food
        self.money = money

    def human_ate(self):
        if self.food > 0:
            self.food -= 1

    def life_flow(self):
        for i_resident in self.residents:
            cube_gen = random.randint(1, 6)
            if i_resident.satiety < 20:
                i_resident.eat()
                self.food -= 1
            elif self.food < 10:
                i_resident.food_shopping()
                self.food += 1
                self.money -= 1
            elif self.money < 50:
                i_resident.work()
                self.money += 1
            elif cube_gen == 1:
                i_resident.work()
                self.money += 1
            else:
                i_resident.play()
            i_resident.print_info()
        self.print_info()

    def print_info(self):
        print(f'Еда в доме: {self.food}; деньги в доме: {self.money}\n')


human_01 = Human('Николай')
human_02 = Human('Петр')
home = Home([human_01, human_02])
for day in range(1, 366):
    print(f'День {day}:')
    if not human_01.is_alive() or not human_02.is_alive():
        break
    home.life_flow()

