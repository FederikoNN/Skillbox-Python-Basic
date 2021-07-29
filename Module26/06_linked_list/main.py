from typing import Any


class Node:
    def __init__(self, value: Any = None, ptr_next=None):
        self.next = ptr_next
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.begin = None
        self.end = None
        self.length = 0

    def __str__(self) -> str:
        curr_ptr = self.begin
        string = '['
        while curr_ptr:
            string += str(curr_ptr.value) + ' '
            curr_ptr = curr_ptr.next
        return string.strip(' ') + ']'

    def append(self, data: Any) -> None:
        self.length += 1
        if not self.begin:
            self.begin = self.end = Node(value=data)
        else:
            self.end.next = self.end = Node(value=data)

    def remove(self, index: int) -> None:
        if not self.begin:
            return
        curr_ptr = self.begin
        prev_ptr = None
        count = 0
        if index == 0:
            self.begin = self.begin.next
            return
        while curr_ptr:
            if count == index:
                if not curr_ptr.next:
                    self.end = curr_ptr
                prev_ptr.next = curr_ptr.next
                break
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next
            count += 1

    def get(self, index: int) -> Any:
        if index == 0:
            curr_ptr = self.begin
            return curr_ptr.value
        curr_ptr = self.begin
        count = 0
        while curr_ptr:
            count += 1
            if count == index:
                return curr_ptr.next.value
            curr_ptr = curr_ptr.next


#
# class Iterator:
#     def __init__(self):
#         self.curr = 0

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
