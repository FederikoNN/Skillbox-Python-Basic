import datetime


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day} \tМесяц: {self.month} \tГод: {self.year}'

    @classmethod
    def from_string(cls, string):
        cls.day = string.split('-')[0]
        cls.month = string.split('-')[1]
        cls.year = string.split('-')[2]
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
