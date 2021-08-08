import functools


def singleton(cls, dict={}):
    # TODO, стоит попробовать уйти от использования словаря в реализации.
    @functools.wraps(cls)
    def wrapp(*args, **kwargs):
        # TODO, стоит проверить, если wrapp.аргумент_декоратора None,
        #  То, присвоить ему значение переменной instance.
        #  После чего, вернуть значение instance.
        if dict:
            return dict[cls.__name__]
        instance = cls(*args, **kwargs)
        dict[cls.__name__] = instance
        return instance

    # TODO, стоит создать аргумент у функции wrapp и присвоить ему значение None.
    #  Пример wrapp.аргумент_декоратора = None

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





# TODO, пожалуйста, обратите внимание, таким образом, если применить декоратор к двум классам,
#  получаем ошибку.


my_obj = Example_2()
my_another_obj = Example_2()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

