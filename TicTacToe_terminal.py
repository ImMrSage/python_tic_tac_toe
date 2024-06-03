from abc import ABC, abstractmethod
from operator import attrgetter
import random

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


class Visual:
    def __init__(self):
        pass

    def show_board(self, board):
        for i in range(0, board.get_rows_count()):
            for j in range(0, board.get_cols_count()):
                item = board.get_elem(i, j)
                symbol = self.get_symbol(item)
                print(symbol, end='\t')
            print()

        print('\n\n')

    def get_symbol(self, value):
        if value == 1:
            return 'X'
        if value == 2:
            return 'O'

        return '_'
    
class Cell:
    def __init__(self, r_idx, c_idx, val):
        self.row_idx = r_idx
        self.col_idx = c_idx
        self.value = val
    
class Level(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_move(self, symbol, board):
        pass


class EasyLevel(Level):
    def __init__(self):
        print('Easy level...')

    def make_move(self, symbol, board):
        row_idx = 0
        col_idx = 0

        while True:
            row_idx = random.randrange(3)
            col_idx = random.randrange(3)

            if board.get_elem(row_idx, col_idx) == 0:
                break

        board.set_elem(row_idx, col_idx, symbol)

class MediumLevel(Level):
    def __init__(self):
        print('Medium level...')

    def make_move(self, symbol, board):

        win_cell = None

         #Horizontals start

        for h in range(0, board.get_rows_count()):
            elem1 = board.get_elem(h, 0)
            elem2 = board.get_elem(h, 1)
            elem3 = board.get_elem(h, 2)

            print("debug:")
            print(elem1, elem2, elem3)

            cells = [Cell(h, 0, elem1), Cell(h, 1, elem2), Cell(h, 2, elem3)]
            cells.sort(key=attrgetter('value'))

            if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
                win_cell = cells[0]

        #Horizontals end

        #Verticals start

        for v in range(0, board.get_cols_count()):
            elem1 = board.get_elem(0, v)
            elem2 = board.get_elem(1, v)
            elem3 = board.get_elem(2, v)

            print("debug:")
            print(elem1, elem2, elem3)

            cells = [Cell(0, v, elem1), Cell(1, v, elem2), Cell(2, v, elem3)]
            cells.sort(key=attrgetter('value'))

            if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
                win_cell = cells[0]

        #Verticals end

        #Main Diagonale start

        elem1 = board.get_elem(0, 0)
        elem2 = board.get_elem(1, 1)
        elem3 = board.get_elem(2, 2)

        print("debug:")
        print(elem1, elem2, elem3)

        cells = [Cell(0, 0, elem1), Cell(1, 1, elem2), Cell(2, 2, elem3)]
        cells.sort(key=attrgetter('value'))

        if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
            win_cell = cells[0]

        #Main diagonale end

        #Secondary diagonale start

        elem1 = board.get_elem(0, 2)
        elem2 = board.get_elem(1, 1)
        elem3 = board.get_elem(2, 0)

        print("debug:")
        print(elem1, elem2, elem3)

        cells = [Cell(0, 2, elem1), Cell(1, 1, elem2), Cell(2, 0, elem3)]
        cells.sort(key=attrgetter('value'))

        if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
            win_cell = cells[0]

        #Secondary diagonale end
    


        if win_cell is not None:
            print("yes, found!")
            print('row idx: ', win_cell.row_idx)
            print('col idx: ', win_cell.col_idx)
            print('symbol: ', win_cell.value)

            board.set_elem(win_cell.row_idx, win_cell.col_idx, symbol)

        else:
            self.make_rand_move(symbol, board)
        



    def make_rand_move(self, symbol, board):
        row_idx = 0
        col_idx = 0

        while True:
            row_idx = random.randrange(3)
            col_idx = random.randrange(3)

            if board.get_elem(row_idx, col_idx) == 0:
                break

        board.set_elem(row_idx, col_idx, symbol)


class HardLevel(Level):
    def __init__(self):
        print('Hard level...')

    def make_move(self, symbol, board):

        win_cell = None

        #Middle 


        if board.get_elem(1, 1) == 0:
            win_cell = Cell(1, 1, 0)
            self.val_move(win_cell, board, symbol)
            return
    

         #Horizontals start

        for h in range(0, board.get_rows_count()):
            elem1 = board.get_elem(h, 0)
            elem2 = board.get_elem(h, 1)
            elem3 = board.get_elem(h, 2)

            print("debug:")
            print(elem1, elem2, elem3)

            cells = [Cell(h, 0, elem1), Cell(h, 1, elem2), Cell(h, 2, elem3)]
            cells.sort(key=attrgetter('value'))

            if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
                win_cell = cells[0]
                self.val_move(win_cell, board, symbol)
                return

        #Horizontals end

        #Verticals start

        for v in range(0, board.get_cols_count()):
            elem1 = board.get_elem(0, v)
            elem2 = board.get_elem(1, v)
            elem3 = board.get_elem(2, v)

            print("debug:")
            print(elem1, elem2, elem3)

            cells = [Cell(0, v, elem1), Cell(1, v, elem2), Cell(2, v, elem3)]
            cells.sort(key=attrgetter('value'))

            if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
                win_cell = cells[0]
                self.val_move(win_cell, board, symbol)
                return

        #Verticals end

        #Main Diagonale start

        elem1 = board.get_elem(0, 0)
        elem2 = board.get_elem(1, 1)
        elem3 = board.get_elem(2, 2)

        print("debug:")
        print(elem1, elem2, elem3)

        cells = [Cell(0, 0, elem1), Cell(1, 1, elem2), Cell(2, 2, elem3)]
        cells.sort(key=attrgetter('value'))

        if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
            win_cell = cells[0]
            self.val_move(win_cell, board, symbol)
            return

        #Main diagonale end

        #Secondary diagonale start

        elem1 = board.get_elem(0, 2)
        elem2 = board.get_elem(1, 1)
        elem3 = board.get_elem(2, 0)

        print("debug:")
        print(elem1, elem2, elem3)

        cells = [Cell(0, 2, elem1), Cell(1, 1, elem2), Cell(2, 0, elem3)]
        cells.sort(key=attrgetter('value'))

        if cells[0].value == 0 and cells[1].value == cells[2].value and cells[1].value != 0:
            win_cell = cells[0]
            self.val_move(win_cell, board, symbol)
            return

        #Secondary diagonale end

        #Corners

        if board.get_elem(0, 0) == 0:
            win_cell = Cell(0, 0, 0)
        elif board.get_elem(0, 2) == 0:
            win_cell = Cell(0, 2, 0)
        elif board.get_elem(2, 0) == 0:
            win_cell = Cell(2, 0, 0)
        elif board.get_elem(2, 2) == 0:
            win_cell = Cell(2, 2, 0)


        if win_cell is not None:
            self.val_move(win_cell, board, symbol)

        else:
            self.make_rand_move(symbol, board)


    def val_move(self, win_cell, board, symbol):

        print("yes, found!")
        print('row idx: ', win_cell.row_idx)
        print('col idx: ', win_cell.col_idx)
        print('symbol: ', win_cell.value)

        board.set_elem(win_cell.row_idx, win_cell.col_idx, symbol)



    def make_rand_move(self, symbol, board):
        row_idx = 0
        col_idx = 0

        while True:
            row_idx = random.randrange(3)
            col_idx = random.randrange(3)

            if board.get_elem(row_idx, col_idx) == 0:
                break

        board.set_elem(row_idx, col_idx, symbol)


class Player(ABC):
    def __init__(self, s):
        self.symbol = s

    @abstractmethod
    def move(self, board):
        pass


class CpuPlayer(Player):
    def __init__(self, s, l):
        super().__init__(s)
        self.level = l

    def move(self, board):
        self.level.make_move(self.symbol, board)


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


class Game:

    def __init__(self):
        self.visual = Visual()
        self.board = Board()
        self.p1 = HumanPlayer(1)
        self.p2 = None

    def opp_menu(self):

            opponent_input = int(input('Please, select your opponent: 1)Human 2)Computer: '))

            if opponent_input == 1:
                self.p2 = HumanPlayer(2)

            elif opponent_input == 2:
                self.comp_menu()

    def comp_menu(self):
          
        menu_input = int(input('Please, choose computer player level: 1)Easy 2)Medium 3)Hard: '))

        if menu_input == 1:
            self.p2 = CpuPlayer(2, EasyLevel())
            
        elif menu_input == 2:
            self.p2 = CpuPlayer(2, MediumLevel())
        
        elif menu_input == 3:
            self.p2 = CpuPlayer(2, HardLevel())
        
        else:
            print('Wrong value')


                

    def start(self):

        self.opp_menu()

        p1Turn = True
        while not self.is_game_over():
            if p1Turn:
                self.p1.move(self.board)
            else:
                self.p2.move(self.board)

            p1Turn = not p1Turn
            self.visual.show_board(self.board)

    def is_game_over(self):
        # Check for a winning condition
        if self.check_winner(1):
            print("Player 1 (X) wins!")
            return True
        elif self.check_winner(2):
            print("Player 2 (O) wins!")
            return True

        # Check for a draw condition
        if self.is_draw():
            print("It's a draw!")
            return True

        return False

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if (
                self.board.get_elem(i, 0) == self.board.get_elem(i, 1) == self.board.get_elem(i, 2) == player
                or self.board.get_elem(0, i) == self.board.get_elem(1, i) == self.board.get_elem(2, i) == player
            ):
                return True

        if (
            self.board.get_elem(0, 0) == self.board.get_elem(1, 1) == self.board.get_elem(2, 2) == player
            or self.board.get_elem(0, 2) == self.board.get_elem(1, 1) == self.board.get_elem(2, 0) == player
        ):
            return True

        return False

    def is_draw(self):
        # Check if all cells are filled (no 0 values)
        for i in range(3):
            for j in range(3):
                if self.board.get_elem(i, j) == 0:
                    return False
        return True







game = Game()
game.start()
