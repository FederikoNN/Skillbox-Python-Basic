class Stack:
    def __init__(self):
        self.object_list = []

    def __str__(self):
        return f'{"; ".join(self.object_list)}'

    def add(self, object_in):
        self.object_list.insert(0, object_in)

    def take(self):
        return self.object_list.pop(0)

    def erase(self):
        return self.object_list.clear()


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def __str__(self):
        return ''.join([f'\n{key} {"; ".join(self.tasks[key])}\n' for key in sorted(self.tasks.keys())])

    def new_task(self, string, priority):
        if priority in self.tasks.keys():
            tmp = Stack()
            tmp.object_list = self.tasks[priority]
            tmp.add(string)
            self.tasks[priority] = tmp.object_list
        else:
            tmp = Stack()
            tmp.add(string)
            self.tasks[priority] = tmp.object_list
        print(self.tasks)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.new_task('выпить воды', 4)
print(manager)

# зачёт!
