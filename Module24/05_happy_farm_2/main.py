class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class GardenPotato:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела\n')
            return False
        else:
            print('Вся картошка созрела!\n')
            return True

    def plant_new(self):
        print('Посадили картошку на грядке\n')
        for i_potato in self.potatoes:
            i_potato.state = 0


class Gardener:
    def __init__(self, name, garden_bed=GardenPotato(5)):
        self.name = name
        self.garden_bed = garden_bed

    def take_care(self):
        print(f'Садовник {self.name} ухаживает за грядкой')
        self.garden_bed.grow_all()

    def harvest(self):
        if self.garden_bed.are_all_ripe():
            print(f'Садовник {self.name} собрал весь урожай!')

            # TODO, это действие по идее, должно убирать старые объекты классов Картошка и добавлять новые.
            #  В таком случае, стоит создать метод у класса GardenPotato, поторый бы добавлял объекты класса
            #  Potato в список potatoes. =)
            self.garden_bed.plant_new()


garden = GardenPotato(5)
gardener = Gardener('Василий', garden)
for _ in range(11):
    gardener.take_care()
    gardener.harvest()
