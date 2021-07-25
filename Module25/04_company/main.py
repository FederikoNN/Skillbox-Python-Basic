class Person:
    def __init__(self, name, age=16):
        self.__name = name
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(16, 90):
            self.__age = age


class Employee(Person):
    def __init__(self, name, age, salary=10000):
        super().__init__(name, age)
        self.__salary = salary

    def salary_accrual(self):
        return self.__salary

    def set_salary(self, amount):
        self.__salary = amount


class Agent(Employee):
    def __init__(self, name, age, sales_volume=0):
        super().__init__(name, age)
        self.sales_volume = sales_volume

    def salary_accrual(self):
        return 5000 + self.sales_volume * 0.05


class Manager(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_salary(13000)


class Worker(Employee):
    def __init__(self, name, age, hours_worked=0):
        super().__init__(name, age)
        self.hours_worked = hours_worked

    def salary_accrual(self):
        return self.hours_worked * 100


employers = [Manager('Bob', 25), Manager('Jlob', 63), Manager('Gleb', 28),
             Agent(name='Ahmad', age=16, sales_volume=105000), Agent(name='Mahmud', age=18, sales_volume=10000),
             Agent(name='Murtaz', age=38, sales_volume=55000), Worker(name='John', age=59, hours_worked=40),
             Worker(name='Bill', age=49, hours_worked=19), Worker(name='Mike', age=35, hours_worked=35)]

for employer in employers:
    print(f'Заработная плата у {employer.get_name()} составляет {employer.salary_accrual()} единиц.')
