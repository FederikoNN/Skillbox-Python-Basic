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

    def intersection_check(self, circle_ext):
        if isinstance(circle_ext, Circle):
            centers_distance = math.sqrt((self.x - circle_ext.x) ** 2 + (self.y - circle_ext.y) ** 2)
            if centers_distance < (circle_ext.radius + self.radius) and centers_distance < abs(
                    circle_ext.radius - self.radius):
                print('Окружности не пересекаются')
            else:
                print('Окружности пересекаются')


circle_01 = Circle()
circle_02 = Circle(0, 2, 1)
print(f'Окружность:\nцентр в точке {circle_01.center}\nрадиус: {circle_01.radius}')
print(f'Площадь окружности: {circle_01.square()}\nПериметр окружности: {circle_01.perimeter()}')
circle_01.zoom_circle(2)
print(circle_01.radius)
circle_01.intersection_check(circle_02)
