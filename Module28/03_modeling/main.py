class Quadratum:
    def __init__(self, segment: float) -> None:
        self.segment = segment

    @property
    def segment(self):
        return self._segment

    @segment.setter
    def segment(self, segment):
        self._segment = segment

    def length(self) -> float:
        return 4 * self._segment

    def square(self) -> float:
        return self._segment ** 2


class Triangle:

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def length(self):
        return self._base + 2 * ((self._base / 2) ** 2 + self._height ** 2) ** 0.5

    def square(self):
        return self._base * self._height * 0.5


class SumSquareMixin:
    def square(self):
        self.set()
        # TODO, пожалуйста, обратите внимание, в классе Mixin вызов этого метода не нужен.
        #  Все необходимые параметры, мы возьмём из методов init.
        return sum([item.square() for item in self.data])


class Cube(SumSquareMixin, Quadratum):
    def __init__(self, segment: float):
        super().__init__(segment)
        self.data = [Quadratum(self.segment) for _ in range(6)]

    # TODO, пожалуйста, обратите внимание, метод получился лишний, т.к. аргумент self.data создаётся в методе init.
    def set(self):
        self.data = [Quadratum(self.segment), Quadratum(self.segment), Quadratum(self.segment),
                     Quadratum(self.segment), Quadratum(self.segment), Quadratum(self.segment)]


class Pyramid(SumSquareMixin, Triangle):
    def __init__(self, base: float, height: float):
        super().__init__(base, height)
        # TODO, стоит уйти от вызова методов внутри метода init и создавать аргумент
        #  self.data именно в этом методе.
        #  Можно просто скопировать код из метода set, а сам метод удалить =)
        self.set()

    def set(self):
        self.data = [Quadratum(self.base), Triangle(self.base, self.height), Triangle(self.base, self.height),
                     Triangle(self.base, self.height), Triangle(self.base, self.height)]


test_01 = Quadratum(1)
print(f'Площадь квадрата со стороной {test_01.segment} = {test_01.square()}')
test_01.segment = 2
print(f'Площадь квадрата со стороной {test_01.segment} = {test_01.square()}')
test_02 = Pyramid(2, 1)
print(
    f'Площадь поверхности пирамиды (высота боковой грани = {test_02.height}; основание= {test_02.base} = {test_02.square()}')
test_02.base = 3
test_02.height = 5
print(
    f'Площадь поверхности пирамиды (высота боковой грани = {test_02.height}; основание= {test_02.base} = {test_02.square()}')

