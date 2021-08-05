import os
from typing import TextIO


class File:
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode

    def __enter__(self) -> TextIO:
        if os.path.exists(self.file_name):
            self.file = open(self.file_name, self.mode, encoding='utf-8')
        else:
            self.file = open(self.file_name, 'w', encoding='utf-8')
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

# зачёт!
