import math


class MyMath:
    PI = math.pi

    @classmethod
    def circle_len(cls, radius) -> float:
        return 2 * cls.PI * radius

    @classmethod
    def circle_sq(cls, radius) -> float:
        return cls.PI * radius ** 2

    @classmethod
    def cube_vol(cls, edge) -> float:
        return edge ** 3

    @classmethod
    def sphere_sq(cls, radius) -> float:
        return 4 * cls.PI * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

# зачёт!
