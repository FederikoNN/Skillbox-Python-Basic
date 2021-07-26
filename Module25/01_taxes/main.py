class Property:
    def __init__(self, tax_percent, worth=0):
        self.worth = worth
        self.tax_percent = tax_percent

    def set_worth(self, worth):
        self.worth = worth

    def tax_calc(self):
        return self.worth * self.tax_percent / 100


class Apartment(Property):

    def __init__(self, tax_percent=0.1, worth=0):
        super().__init__(tax_percent, worth)
        self.worth = worth
        self.tax_percent = tax_percent

    def __str__(self):
        return 'Квартира'


class Car(Property):
    def __init__(self, tax_percent=0.5, worth=0):
        super().__init__(tax_percent, worth)
        self.worth = worth
        self.tax_percent = tax_percent

    def __str__(self):
        return 'Автомобиль'


class CountryHouse(Property):
    def __init__(self, tax_percent=0.2, worth=0):
        super().__init__(tax_percent, worth)
        self.worth = worth
        self.tax_percent = tax_percent

    def __str__(self):
        return 'Дача'


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
