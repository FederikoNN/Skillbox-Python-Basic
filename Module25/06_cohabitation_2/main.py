import random


class FamilyMember:
    # TODO, стоит добавить человеку аргумент "дом" изначально равный None
    #  И метод, в котором присвоим человеку дом. =)

    def __init__(self, name, home, satiety=0, happiness=0):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.home = home

    def get_name(self):
        return self.name

    def eat(self):
        print(f'{self.name} кушает')
        if self.satiety >= 0:
            feed = random.randint(0, 30)
            self.satiety += feed
            self.home.food -= feed
            self.home.eaten += feed

    # TODO, т..к у жены этих методов нет, то создавать пустые методы не нужно =)
    def work(self):
        pass

    def play(self):
        pass

    def is_alive(self):
        if self.satiety < 0:
            print(f'{self.name} от таких нагрузок всё...')
            return False
        return True

    def is_happiness(self):
        if self.happiness < 10:
            print(f'{self.name} полностью в себе из-за депрессии...')
            return False
        return True

    def print_info(self):
        print(f'{self.name} сытость: {self.satiety}; степень счастья: {self.happiness}')


class Husband(FamilyMember):
    # TODO, если метод не переопределяется, то создавать его не нужно! =)
    def __init__(self, name, home, satiety=30, happiness=100):
        super().__init__(name, home, satiety, happiness)

    def work(self):
        print(f'{self.name} работает')
        self.satiety -= 10
        self.home.money += 150
        self.home.earned += 150

    def play(self):
        print(f'{self.name} решил поиграть')
        if self.satiety > 0:
            self.satiety -= 10
            self.happiness += 20

    def caress_cat(self):
        print(f'{self.name} гладит кота')
        self.happiness += 5
        self.satiety -= 10

    def one_day_of_life(self):
        cube_gen = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.money < 50:
            self.work()
        elif cube_gen == 1:
            self.work()
        elif cube_gen in range(2, 4):
            self.caress_cat()
        else:
            self.play()
        self.print_info()


class Wife(FamilyMember):
    def __init__(self, name, home, satiety=30, happiness=100, furs=0):
        super().__init__(name, home, satiety, happiness)
        self.furs = furs

    def food_shopping(self, quantity):
        if self.home.money >= 10 * quantity:
            print(f'{self.name} сходилa в магазин за продуктами')
            self.home.money -= 10 * quantity
            self.home.food += 10 * quantity
            if self.home.cats_food < 20:
                self.home.money -= 10
                self.home.cats_food += 10
            self.satiety -= 10

    def buy_furs(self):
        if self.home.money > 360:
            print(f'{self.name} шубу себе купила!')
            self.home.money -= 350
            self.satiety -= 10
            self.happiness += 60
            self.furs += 1

    def caress_cat(self):
        print(f'{self.name} гладит кота')
        self.happiness += 5
        self.satiety -= 10

    def clean_house(self):
        print(f'{self.name} навела порядок в доме')
        self.home.dirt -= random.randint(10, 100)
        if self.home.dirt < 0:
            self.home.dirt = 0
        self.satiety -= 10

    def one_day_of_life(self):
        cube_gen = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.food < 30:
            self.food_shopping(cube_gen)
        elif self.home.dirt > 50:
            self.clean_house()
        elif self.home.money > 370:
            self.buy_furs()
        elif cube_gen == 1:
            self.clean_house()
        elif cube_gen in range(2, 4):
            self.eat()
        else:
            self.caress_cat()
        self.print_info()


class Cat(FamilyMember):
    # TODO, если метод не переопределяется, то создавать его не нужно!
    def __init__(self, name, home, satiety=30, happiness=0):
        super().__init__(name, home, satiety, happiness)

    def eat(self):
        print(f'Кот {self.name} покушал')
        if self.satiety >= 0:
            feed = random.randint(0, 10)
            self.satiety += feed
            self.home.cats_food -= feed / 2
            self.home.eaten_cat += feed / 2

    def sleep(self):
        self.satiety -= 10

    def tear_up(self):
        self.satiety -= 10
        self.home.dirt += 5

    def print_info(self):
        print(f'Кот {self.name} сытость: {self.satiety}')

    def one_day_of_life(self):
        cube_gen = random.randint(1, 3)
        if self.satiety < 20:
            self.eat()
        elif cube_gen == 1:
            self.eat()
        elif cube_gen == 2:
            self.tear_up()
        else:
            self.sleep()
        self.print_info()


class Home:
    def __init__(self, resident=None, food=50, cats_food=30, money=100, dirt=0, earned=0, eaten=0, eaten_cat=0):
        self.residents = []
        self.food = food
        self.cats_food = cats_food
        self.money = money
        self.add_resident(resident)
        self.dirt = dirt
        self.earned = earned
        self.eaten = eaten
        self.eaten_cat = eaten_cat

    def add_resident(self, member):
        if isinstance(member, FamilyMember):
            self.residents.append(member)

    def life_flow(self):
        for i_resident in self.residents:
            i_resident.one_day_of_life()
        self.print_info()

    def print_info(self):
        print(
            f'\nЕда в доме: {self.food}; деньги в доме: {self.money}\nеда для кота: {self.cats_food}; грязь в доме: {self.dirt}\n')


home_sweet = Home()
husband = Husband(name='Николай', home=home_sweet)
wife = Wife(name='Ольга', home=home_sweet)
cat = Cat(name='Анимподист', home=home_sweet)
home_sweet.add_resident(husband)
home_sweet.add_resident(wife)
home_sweet.add_resident(cat)

for day in range(1, 366):
    print(f'День {day}:')
    if not husband.is_alive() or not wife.is_alive():
        break
    if not husband.is_happiness() or not wife.is_happiness():
        break

    # TODO, предлагаю перенести эту проверку в классы Мужа и Жены, или в FamilyMember.
    #  Но, в таком случае, класс FamilyMember не должен быть родительским у кота =)
    if home_sweet.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
    home_sweet.life_flow()
    home_sweet.dirt += 5
print(f'За год было заработано {home_sweet.earned} денег, съедено еды: {home_sweet.eaten} единиц,'
      f' съедено котом {home_sweet.eaten_cat} единиц еды.\nЗато жена купила {wife.furs} шуб!')
