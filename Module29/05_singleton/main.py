import functools

obj_list = []


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
