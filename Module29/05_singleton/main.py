import functools


def singleton(cls, dict={}):
    @functools.wraps(cls)
    def wrapp(*args, **kwargs):
        if dict:
            return dict[cls.__name__]
        instance = cls(*args, **kwargs)
        dict[cls.__name__] = instance
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
