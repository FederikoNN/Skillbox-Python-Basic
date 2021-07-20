import random


class Warrior:

    def __init__(self, number, health=100):
        self.number = number
        self.health = health
        self.name = f'Воин {number}'

    def attack_in(self, unit):
        if isinstance(unit, Warrior):
            unit.health -= 20
            if unit.health >= 0:
                print(f'У Воина {unit.number} осталось здоровья: {unit.health}')
            else:
                print(f'{unit.name} погиб...')

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
            print(f'Атаковал {self.warriors[num % 2].name}')
            self.warriors[num % 2].attack_in(self.warriors[num // 2])
            if self.warriors[num // 2].is_defeated():
                print(f'{self.warriors[num % 2].name} одержал победу!')
                break
            input('Нажмите любую клавишу для продолжения...')


fight = Fight()
fight.fray()
