import random


class KillError:
    def __str__(self):
        return 'вызвано исключение KillError'


class DrunkError:
    def __str__(self):
        return 'вызвано исключение DrunkError'


class CarCrashError:
    def __str__(self):
        return 'вызвано исключение CarCrashError'


class GluttonyError:
    def __str__(self):
        return 'вызвано исключение GluttonyError'


class DepressionError:
    def __str__(self):
        return 'вызвано исключение DepressionError'


class Karma:
    __exceptions = [DepressionError(), KillError(), CarCrashError(), DepressionError(), GluttonyError()]
    __karma_purpose = 500

    def __init__(self, karma_score=0):
        self.karma = karma_score

    def get_karma_purpose(self):
        return self.__karma_purpose

    def get_exceptions(self):
        return self.__exceptions


class BuddhistLife(Karma):
    def one_day(self):
        if self.karma < 0:
            self.karma = 0
        if random.randint(1, 10) == 1:
            # self.karma -= 50
            raise Exception(random.choice(self.get_exceptions()))
        self.karma += random.randint(1, 7)
        return self.karma


buddhist = BuddhistLife()
days_count = 0
with open('karma.log', 'w') as file:
    while True:
        days_count += 1
        try:
            buddhist.one_day()
        except Exception as msg:
            buddhist.karma = buddhist.karma - 50
            file.write(f'На {days_count} день {msg}\n')
        if buddhist.karma >= buddhist.get_karma_purpose():
            print(f'Просветление достигнуто за {days_count} дней!')
            break
