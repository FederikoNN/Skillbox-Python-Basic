from collections.abc import Iterable
from typing import Any


class SquareNum:
    def __init__(self, number: int) -> None:
        self.cur_number = 0
        self.number = number

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> Any:
        self.cur_number += 1
        if self.cur_number > self.number:
            raise StopIteration
        return self.cur_number ** 2


def square_num(number: int) -> Iterable[int]:
    for num in range(1, number + 1):
        yield num ** 2


N = int(input('Введите число: '))
for squ_num in SquareNum(N):
    print(squ_num)

for value in square_num(N):
    print(value, end=' ')

square_gen = (num ** 2 for num in range(1, N + 1))
for value in square_gen:
    print(value, end=' ')

# зачёт!
