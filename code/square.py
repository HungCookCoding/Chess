

class Square:

    def __init__(self, row, col, piece = None):
        self.row = row 
        self.col = col 
        self.piece = piece

    def have_piece(self):
        return self.piece != None
    
    def name_piece(self):
        if self.have_piece():
            return self.piece.name
        return '-'
    
    def color_piece(self):
        if self.have_piece():
            return self.piece.color
        return '-'