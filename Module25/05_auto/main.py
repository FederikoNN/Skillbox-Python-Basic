import math


class Vehicle:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.angle = angle

    def move(self, distance):
        self.x = self.x + math.cos(math.radians(self.angle)) * distance
        self.y = self.y + math.sin(math.radians(self.angle)) * distance
        self.coordinates = (round(self.x, 2), round(self.y, 2))

    def turn(self, angle):
        self.angle = self.angle + angle


class Bus(Vehicle):
    def __init__(self, passengers, x=0, y=0, angle=0, money=0):
        super().__init__(x, y, angle)
        self.passengers = passengers
        self.money = money

    def enter(self, count):
        self.passengers += count

    def exit(self, count):
        if count < self.passengers:
            self.passengers -= count
            return
        self.passengers = 0

    def move(self, distance):
        self.x = self.x + math.cos(math.radians(self.angle)) * distance
        self.y = self.y + math.sin(math.radians(self.angle)) * distance
        self.coordinates = (round(self.x, 2), round(self.y, 2))
        self.money += (distance // 10) * 2 * self.passengers


bus = Bus(passengers=52, angle=50, x=5)
bus.move(1052)
print(f'Координаты конечной остановки:{bus.coordinates}\nЗаработано денег: {bus.money}')
bus.exit(50)  # вышло 50 пассажиров
bus.enter(56)  # вошло 56 пассажиров
bus.turn(180)  # развернулись на 180 градусов
bus.move(1052)  # поехали на остановку отправления
print(f'Координаты начальной остановки:{bus.coordinates}\nЗаработано денег: {bus.money}')
