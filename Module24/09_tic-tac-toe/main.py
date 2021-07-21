import random


class TicTacToe:

    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def __init__(self, table=None):
        if table is None:
            table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.table = table
        self.list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.list_player = []
        self.list_comp = []

    def print_table(self):
        print('\t' * 8, '  Номера ячеек')
        print('\t     |     |\t\t\t' * 2)
        print(f'\t  {self.table[0]}  |  {self.table[1]}  |  {self.table[2]}\t\t\t\t  {1}  |  {2}  |  {3}')
        print('\t_____|_____|_____\t\t' * 2)
        print('\t     |     |\t\t\t' * 2)
        print(f'\t  {self.table[3]}  |  {self.table[4]}  |  {self.table[5]}\t\t\t\t  {4}  |  {5}  |  {6}')
        print('\t_____|_____|_____\t\t' * 2)
        print('\t     |     |\t\t\t' * 2)
        print(f'\t  {self.table[6]}  |  {self.table[7]}  |  {self.table[8]}\t\t\t\t  {7}  |  {8}  |  {9}')
        print('\t     |     |\t\t\t' * 2)

    def player_step(self, num):
        if num in self.list_num:
            self.list_player.append(self.list_num.pop(self.list_num.index(num)))
            # self.list_comp.append(num)
            # self.list_num.remove(num)
            self.table[num - 1] = 'X'
            if self.check_win(self.list_player, 'Игрок'):
                return True

    def comp_step(self):
        num = random.choice(self.list_num)
        self.list_comp.append(self.list_num.pop(self.list_num.index(num)))
        # self.list_comp.append(num)
        # self.list_num.remove(num)
        self.table[num - 1] = 'O'
        if self.check_win(self.list_comp, 'Компьютер'):
            return True
        return False

    def check_win(self, list_in, name):
        for i_set in self.win_combinations:
            if set(i_set).issubset(list_in):
                print(f'Выиграл {name}!')
                return True
        return False


while True:
    game = TicTacToe()
    step = 1
    game.print_table()
    while game.list_num:
        print(f'\n{step}- й ход!')
        while True:
            choice = int(input('Выберите ячейку: '))
            if choice in game.list_num:
                break
            print('Ошибка ввода!')
        if game.player_step(choice):
            break
        if not game.list_num:
            print('Ничья!')
            break
        if game.comp_step():
            break
        game.print_table()
        step += 1
    input('\nНажмите любую клавишу!')

