import random


# TODO, пожалуйста, обратите внимание, необходимо создать 5 классов исключений и хранить в списке __exceptions именно их.

class Karma:
    __exceptions = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
    __karma_purpose = 500

    def __init__(self, karma_score=0):
        self.karma = karma_score

    def get_karma_purpose(self):
        return self.__karma_purpose

    def get_exceptions(self):
        return self.__exceptions


class BuddhistLife(Karma):
    # TODO, если метод не переопределяется, то создавать его не нужно! =)
    def __init__(self, karma=0):
        super().__init__(karma)

    def one_day(self):
        if self.karma < 0:
            self.karma = 0
        if random.randint(1, 10) == 1:
            # self.karma -= 50
            raise Exception  # TODO, вызывать необходимо исключение из списка __exceptions.
        self.karma += random.randint(1, 7)
        return self.karma


buddhist = BuddhistLife()
days_count = 0
with open('karma.log', 'w') as file:
    while True:
        days_count += 1
        try:
            buddhist.one_day()
        except Exception:
            buddhist.karma = buddhist.karma - 50
            file.write(f'На {days_count} день возникло исключение {random.choice(buddhist.get_exceptions())}\n')
        if buddhist.karma >= buddhist.get_karma_purpose():
            print(f'Просветление достигнуто за {days_count} дней!')
            break
