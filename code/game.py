
from const import *
from square import Square
from piece import *
from move import Move

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

        self.click = []
        self.square_click = ()

        self.turn_white = True
        self.check_mate = False
        self.stale_mate = False

        self.moved = []     #lưu trữ nước đi
        self.valid_moves = self.get_possible_move()


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


    def make_move(self, move):
        self.board[move.start[0]][move.start[1]] = Square(move.start[0], move.start[1])
        self.board[move.end[0]][move.end[1]] = Square(move.end[0], move.end[1], move.piece_moved)
        self.turn_white = not self.turn_white
        self.moved.append(move)

    def undo_move(self):
        if len(self.moved) != 0:
            move = self.moved.pop()
            self.board[move.start[0]][move.start[1]] = Square(move.start[0], move.start[1], move.piece_moved)
            self.board[move.end[0]][move.end[1]] = Square(move.end[0], move.end[1], move.piece_captured)
            self.turn_white = not self.turn_white

    def get_possible_move(self):
        moves = []

        for row in range(ROW):
            for col in range(COL):
                color = self.board[row][col].color_piece()
                name = self.board[row][col].name_piece()
                if (color == 'W' and self.turn_white) or (color == 'B' and not self.turn_white):
                    if name == 'Pawn': 
                        self.move_pawn(row, col, color, moves)
        
        
        return moves

    def move_pawn(self, row, col, color, moves):
        dir = -1 if color == 'W' else 1              #hướng đi của tốt

        if color == 'W':
            moved = False if row == 6 else True      #xác định quân tốt đã di chuyển chưa
        else:
            moved = False if row == 1 else True
        
        enemy = 'B' if color == 'W' else 'W'         #xác định quân địch
        
        if not self.board[row+1*dir][col].have_piece():
            moves.append(Move((row, col), (row+1*dir, col), self.board))
            if not moved and not self.board[row+2*dir][col].have_piece():
                moves.append(Move((row, col), (row+2*dir, col), self.board))
        if col+1 <= 7:
            if self.board[row+1*dir][col+1].color_piece() == enemy:
                moves.append(Move((row, col), (row+1*dir, col+1), self.board))
        if col-1 >= 0:
            if self.board[row+1*dir][col-1].color_piece() == enemy:
                moves.append(Move((row, col), (row+1*dir, col-1), self.board))
    
    def move_knight(self, row, col, color, moves):
        dir = ()
    
    def move_bishop(self, row, col, color, moves):
        pass

    def move_rook(self, row, col, color, moves):
        pass

    def move_queen(self, row, col, color, moves):
        pass

    def move_king(self, row, col, color, moves):
        pass