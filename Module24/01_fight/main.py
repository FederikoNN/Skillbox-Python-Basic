import random


class Warrior:

    def __init__(self, number, health=100):
        self.number = number
        self.health = health
        self.name = f'Воин {number}'

    def attack_in(self):
        # TODO, по идее, этот метод должен принимать на вход объект Warrior
        #  Проверять, является ли он объектом класса Warrior и наносить урон ему, а не себе.
        #  Давайте немного поправим.

        self.health -= 20
        if self.health >= 0:
            print(f'У Воина {self.number} осталось здоровья: {self.health}')
        else:
            print(f'{self.name} погиб...')

    def is_defeated(self):
        if self.health >= 0:
            return False
        return True


class Fight:

    def __init__(self):
        self.warriors = [Warrior(index) for index in range(1, 3)]

    def fray(self):
        while True:
            num = random.randint(1, 2)
            print(f'Атаковал {self.warriors[num // 2].name}')
            self.warriors[num % 2].attack_in()
            if self.warriors[num % 2].is_defeated():
                print(f'{self.warriors[num // 2].name} одержал победу!')
                break
            input('Нажмите любую клавишу для продолжения...')


fight = Fight()
fight.fray()
