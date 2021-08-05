import datetime


class Date:
    def __init__(self, day: str, month: str, year: str) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day} \tМесяц: {self.month} \tГод: {self.year}'

    @classmethod
    def from_string(cls, string):
        # TODO Создавать переменные лучше без использования cls.
        #  Т.к. нам необходимо вернуть не новый объект класса Date, а текущий, передав в него эти переменные.
        cls.day, cls.month, cls.year = string.split('-')
        return Date(cls.day, cls.month, cls.year)

    @classmethod
    def is_date_valid(cls, string):
        try:
            datetime.datetime.strptime(string, '%d-%m-%Y')
        except BaseException:
            return False
        return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# зачёт!
