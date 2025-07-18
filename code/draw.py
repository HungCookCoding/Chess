
import pygame
from const import *
from game import Game

class Draw:

    def __init__(self):
        self.game = Game()

    def draw_board(self, surface):
        for row in range(ROW):
            for col in range(COL):
                rect = (row * SQSIZE, col * SQSIZE, SQSIZE, SQSIZE)
                if (row + col) %2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                
                pygame.draw.rect(surface, color, rect)

    def draw_piece(self, surface, board):
        for row in range(ROW):
            for col in range(COL):
                if board[row][col].have_piece():
                    rect = (col * SQSIZE, row * SQSIZE)
                    surface.blit(board[row][col].piece.img, rect)
                