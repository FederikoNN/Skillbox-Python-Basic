class Water:

    def __init__(self, name='Вода'):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}'

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
        return f'{self.__class__.__name__}'

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
        return f'{self.__class__.__name__}'

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
        return f'{self.__class__.__name__}'

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
    answer = f'{Water().name} + {Air().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Steam:
    name = 'Пар'
    answer = f'{Water().name} + {Fire().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Dirt:
    name = 'Грязь'
    answer = f'{Water().name} + {Terra().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Lightning:
    name = 'Молния'
    answer = f'{Air().name} + {Fire().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Dust:
    name = 'Пыль'
    answer = f'{Terra().name} + {Air().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Lava:
    name = 'Лава'
    answer = f'{Terra().name} + {Fire().name} = {name}'

    def __str__(self):
        return f'{self.__class__.__name__}'


element_01 = Water()
element_02 = Terra()
element_derived = element_01 + element_02
if element_derived:
    print(element_derived.answer)
else:
    print(f'{element_01.name} + {element_02.name} = {element_derived}')

print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Air(), '+', Fire(), '=', Air() + Fire())
