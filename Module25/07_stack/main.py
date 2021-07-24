class Stack:
    def __init__(self, object_list=[]):
        self.object_list = object_list

    def __str__(self):
        return f'{"; ".join(self.object_list)}'

    def add(self, object_in):
        self.object_list.insert(0, object_in)

    def take(self):
        return self.object_list.pop(0)

    def erase(self):
        return self.object_list.clear()


class TaskManager:
    def __init__(self, tasks={}, stack=Stack()):
        self.tasks = tasks
        self.stack = stack

    def __str__(self):
        return ''.join([f'\n{key} {"; ".join(self.tasks[key])}\n' for key in sorted(self.tasks.keys())])

    def new_task(self, string, priority):
        if priority in self.tasks.keys():
            self.stack = Stack(self.tasks[priority])
            self.stack.add(string)
            self.tasks[priority] = self.stack.object_list
        else:
            self.stack = Stack([string])
            self.tasks[priority] = self.stack.object_list


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
