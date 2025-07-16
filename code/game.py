
from const import *
from square import Square
from piece import *

class Game:

    def __init__(self):
        self.board = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
                      ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['--', '--', '--', '--', '--', '--', '--', '--'],
                      ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                      ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']]
        self.create_board()


    def create_board(self):
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece != '--':
                    if piece[1] == 'P': self.board[row][col] = Square(row, col, Pawn(piece[0]))
                    elif piece[1] == 'N': self.board[row][col] = Square(row, col, Knight(piece[0]))
                    elif piece[1] == 'B': self.board[row][col] = Square(row, col, Bishop(piece[0]))
                    elif piece[1] == 'R': self.board[row][col] = Square(row, col, Rook(piece[0]))
                    elif piece[1] == 'Q': self.board[row][col] = Square(row, col, Queen(piece[0]))
                    elif piece[1] == 'K': self.board[row][col] = Square(row, col, King(piece[0]))
                else:
                    self.board[row][col] = Square(row, col)