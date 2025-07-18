

class Move:

    rank_row = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
    rank_col = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: "h"}

    def __init__(self, start, end, board):
        self.start = start
        self.end = end 
        self.piece_moved = board[start[0]][start[1]].piece
        self.piece_captured = board[end[0]][end[1]].piece


    def __eq__(self, other):
        return self.start == other.start and self.end == other.end          #định nghĩa cách so sánh 2 đối tượng là giống nhau lớp Move


    def chess_loca(self, row, col):
        return self.rank_row[row] + self.rank_col[col]
    
    def move_loca(self, start, end):
        return self.chess_loca(start[0], start[1]) + self.chess_loca(end[0], end[1])