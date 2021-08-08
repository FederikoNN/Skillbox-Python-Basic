import functools

obj_list = []


# TODO, пожалуйста, обратите внимание, т.к. синглотон говорит о том, что объект класса будет один,
#  Стоит решить задание без использования дополнительного списка obj_list.
#  Если учесть, что всё в python является объектами класса, возможно будет лучше создать аргумент у функции декоратора
#  и присвоить значение объекта класса ему. Помните, как мы создавали аргумент для подсчёта количества вызовов функций
#  в предыдущем уроке?


def singleton(cls):
    @functools.wraps(cls)
    def wrapp(*args, **kwargs):
        if obj_list:
            return obj_list[0]
        instance = cls(*args, **kwargs)
        obj_list.append(instance)
        return instance

    return wrapp


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
