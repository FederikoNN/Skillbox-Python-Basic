class QHofstadter:
    def __init__(self, list_in: list) -> None:
        self.counter = 2
        if list_in[0] == list_in[1] == 1:
            self.list_in = list_in
        else:
            raise StopIteration('Последовательность завершилась')

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.list_in.append(self.list_in[self.counter - self.list_in[self.counter - 1]] + self.list_in[
            self.counter - self.list_in[self.counter - 2]])
        self.counter += 1
        return self.list_in[self.counter - 1]


try:
    q_sequence = QHofstadter([1, 1])
    N = int(input('Сколько элементов последовательности вывести: '))
    for i_elem in range(1, N + 1):
        if i_elem == 1 or i_elem == 2:
            print(f'{i_elem} элемент последовательности Q Хофштадтера: \t1')
            continue
        print(f'{i_elem} элемент последовательности Q Хофштадтера: \t{next(q_sequence)}')
except StopIteration as msg:
    print(msg)
