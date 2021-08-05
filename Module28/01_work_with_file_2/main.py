import os
from typing import TextIO


class File:
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode

    def __enter__(self) -> TextIO:
        if os.path.exists(self.file_name):
            # TODO, если мы записываем в файл русские символы, или выводим их из файла, то
            #  стоит использовать кодировку utf-8, иначе, пользователи Windows, не смогу прочитать данные из файла. =)
            self.file = open(self.file_name, self.mode)
        else:
            self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!\n')

with File('example.txt', 'r') as file:
    file.write('Всем привет!\n')

with File('example.txt', 'a') as file:
    file.write('Всем пока!')
