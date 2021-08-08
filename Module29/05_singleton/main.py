import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapp(*args, **kwargs):
        if wrapp.is_cls:
            return wrapp.is_cls
        instance = cls(*args, **kwargs)
        wrapp.is_cls = instance
        return instance

    wrapp.is_cls = None
    return wrapp


@singleton
class Example:
    pass


@singleton
class Example_2:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

my_obj = Example_2()
my_another_obj = Example_2()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# зачёт!
