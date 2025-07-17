
import pygame
from const import *

class Piece:

    def __init__(self, name, color, value):
        self.name = name 
        self.color = color 
        self.value = value
        self.img = pygame.transform.scale(pygame.image.load('img/' + self.color + self.name + '.png'), (SQSIZE, SQSIZE))
    

class Pawn(Piece):
    
    def __init__(self, color):
        super().__init__('Pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('Knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('Bishop', color, 3.0)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('Rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('Queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        super().__init__('King', color, 1000.0)
