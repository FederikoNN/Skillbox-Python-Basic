class Water:
    name = 'Вода'

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
    name = 'Воздух'

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
    name = 'Огонь'

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
    name = 'Земля'

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
    answer = f'{Water.name} + {Air.name} = {name}'


class Steam:
    # name = 'Пар'
    answer = f'{Water.name} + {Fire.name} = Пар'


class Dirt:
    name = 'Грязь'
    answer = f'{Water.name} + {Terra.name} = {name}'


class Lightning:
    name = 'Молния'
    answer = f'{Air.name} + {Fire.name} = {name}'


class Dust:
    name = 'Пыль'
    answer = f'{Terra.name} + {Air.name} = {name}'


class Lava:
    name = 'Лава'
    answer = f'{Terra.name} + {Fire.name} = {name}'


element_01 = Air()
element_02 = Terra()
element_derived = element_01 + element_02
if element_derived:
    print(element_derived.answer)
else:
    print(f'{element_01.name} + {element_02.name} = {element_derived}')
