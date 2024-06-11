
import tkinter as tk
from abc import ABC, abstractmethod
import random

# Board class from TicTacToe_terminal.py
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

# Player classes from TicTacToe_terminal.py
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def make_move(self, board, row_idx, col_idx):
        board.set_elem(row_idx, col_idx, self.symbol)

class ComputerPlayer(Player):
    def make_move(self, board):
        while True:
            row_idx = random.randrange(3)
            col_idx = random.randrange(3)
            if board.get_elem(row_idx, col_idx) == 0:
                board.set_elem(row_idx, col_idx, self.symbol)
                break

# Check win function from TicTacToe_terminal.py
def check_win(board, symbol):
    for i in range(3):
        if all(board.get_elem(i, j) == symbol for j in range(3)):
            return True
        if all(board.get_elem(j, i) == symbol for j in range(3)):
            return True
    if all(board.get_elem(i, i) == symbol for i in range(3)):
        return True
    if all(board.get_elem(i, 2 - i) == symbol for i in range(3)):
        return True
    return False

# Visual interface from tictactoe_visual.py
root = tk.Tk()
root.title("Tic Tac Toe")
play_area = tk.Frame(root)
current_chr = "X"
status = True
board = Board()
human_player_1 = HumanPlayer(1)
human_player_2 = HumanPlayer(2)

class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr, status
        if not self.value and status:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            row_idx = self.x - 1
            col_idx = self.y - 1
            player_symbol = 1 if current_chr == "X" else 2
            board.set_elem(row_idx, col_idx, player_symbol)

            if check_win(board, player_symbol):
                print(f'Player {current_chr} wins')
                status = False

            current_chr = "O" if current_chr == "X" else "X"

    def reset(self):
        self.button.configure(text="", bg='white')
        self.value = None

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

play_area.pack(pady=10, padx=10)
root.mainloop()
