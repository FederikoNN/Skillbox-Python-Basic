import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.center = (x, y)

    def square(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.radius * math.pi

    def zoom_circle(self, K):
        self.radius = K * self.radius

    def intersection_check(self, x, y, radius):
        # TODO, в этот метод предлага добавлять обхект класса Круг,
        #  стоит добавить проверку, что элемент является объектом класса Круг.
        #  Ведь в противном случае, он может не иметь аргументов "x" и "y"
        #  Таким образом, у метода будет всего один параметр, вместо трёх =)

        centers_distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        if centers_distance < (radius + self.radius) and centers_distance < abs(radius - self.radius):
            print('Окружности не пересекаются')
        else:
            print('Окружности пересекаются')


circle = Circle()
print(f'Окружность:\nцентр в точке {circle.center}\nрадиус: {circle.radius}')
print(f'Площадь окружности: {circle.square()}\nПериметр окружности: {circle.perimeter()}')
# circle.zoom_circle(3)
# print(circle.radius)
# circle.intersection_check(0, 2, 1)
