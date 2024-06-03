import tkinter as tk
from abc import ABC, abstractmethod
from operator import attrgetter
import random

root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

play_area = tk.Frame(root, width=300, height=300, bg='white')

class Board:

    def __init__(self):
        self.matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def set_elem(self, row_idx, col_idx, elem):
        self.matrix[row_idx][col_idx] = elem

    def get_elem(self, row_idx, col_idx):
        return self.matrix[row_idx][col_idx]

    def get_rows_count(self):
        return len(self.matrix)

    def get_cols_count(self):
        return len(self.matrix[0])

board = Board()

class Player(ABC):
    def __init__(self, s):
        self.symbol = s

    @abstractmethod
    def move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, s):
       super().__init__(s)

    def move(self, board):
        row_idx = 0
        col_idx = 0

        while True:
            row_input = int(input('enter row [1;3]: '))
            col_input = int(input('enter col [1;3]: '))

            row_idx = row_input - 1
            col_idx = col_input - 1

            if board.get_elem(row_idx, col_idx) == 0:
                break

        board.set_elem(row_idx, col_idx, self.symbol)

human_player_1 = HumanPlayer(1)
human_player_2 = HumanPlayer(2)



current_chr = "X"
status = True

class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        global status
        print(status)
        if status == False:
            return
        if not self.value and status == True:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            print(f'Coordinates: {self.x}, {self.y}')
            row_idx = self.x - 1
            col_idx = self.y - 1
            player_symbol = 0
            if current_chr == "X":
                player_symbol = human_player_1.symbol
            else:
                player_symbol = human_player_2.symbol
            board.set_elem(row_idx, col_idx, player_symbol)
            for i in range(0, 3):
                for j in range(0, 3):
                    print(board.get_elem(i, j), end=' ')
                print()
            self.check_win()

            if current_chr == "X":
                current_chr = "O"
            elif current_chr == "O":
                current_chr = "X"

    def check_win(self):
        for i in range(0, 3):
            elem1 = board.get_elem(i, 0)
            elem2 = board.get_elem(i, 1)
            elem3 = board.get_elem(i, 2)
            if elem1 == elem2 and elem2 == elem3 and elem1 != 0:
                print(f'Player {elem1} wins')
                status = False
                print(status)


    def reset(self):
        self.button.configure(text="", bg='white')
        self.value = None

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)
play_area.pack(pady=10, padx=10)

root.mainloop()
