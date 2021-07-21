class Water:

    def __init__(self, name='Вода'):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Terra):
            return Dirt()
        else:
            return None


class Air:
    def __init__(self, name='Воздух'):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Terra):
            return Dust()
        else:
            return None


class Fire:
    def __init__(self, name='Огонь'):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Terra):
            return Lava()
        else:
            return None


class Terra:
    def __init__(self, name='Земля'):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        else:
            return None


class Storm:
    name = 'Шторм'

    def __str__(self):
        return f'{self.name}'


class Steam:
    name = 'Пар'

    def __str__(self):
        return f'{self.name}'


class Dirt:
    name = 'Грязь'

    def __str__(self):
        return f'{self.name}'


class Lightning:
    name = 'Молния'

    def __str__(self):
        return f'{self.name}'


class Dust:
    name = 'Пыль'

    def __str__(self):
        return f'{self.name}'


class Lava:
    name = 'Лава'

    def __str__(self):
        return f'{self.name}'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Air(), '+', Fire(), '=', Air() + Fire())
