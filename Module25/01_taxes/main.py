class Property:
    def __init__(self, worth=0):
        self.worth = worth
        # TODO, предлагаю сократить количество вызовов методов в методе init
        #  и создавать в нём только аргументы, которые класс использует в работе.
        self.set_worth(worth)

    def set_worth(self, worth):
        pass

    def tax_calc(self):
        return self.worth / 1000


class Apartment(Property):
    # TODO, если метод не переопределяется, то создавать его не нужно!
    #  Но, в разрезе данного задания, предлагаю добавить в него аргумент "процент стоимости"
    #  и использовать его в методе с расчётом налога, вместо чисел 1000, 500 и 200.
    #  В таком случае, если число в дальнейшем нужно будет поменять, мы всегда легко найдём его
    #  в методе init.

    def __init__(self, worth=0):
        super().__init__(worth)

    def __str__(self):
        return 'Квартира'


class Car(Property):
    def __init__(self, worth=0):
        super().__init__(worth)

    def __str__(self):
        return 'Автомобиль'

    def tax_calc(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth=0):
        super().__init__(worth)

    def __str__(self):
        return 'Дача'

    def tax_calc(self):
        return self.worth / 500


property_list = [Apartment(), Car(), CountryHouse()]
money = int(input('И сколько у Вас денег? '))
taxes = 0
for i_property in property_list:
    i_property.set_worth(int(input(f'Сколько стоит {i_property}: ')))
    taxes += i_property.tax_calc()
    print(f'Налог на {i_property}:', i_property.tax_calc())
if taxes > money:
    print(f'Вам не хватает {taxes - money} денег на налоги!')
else:
    print('Денег на налоги хватает. Можно спать спокойно.')
