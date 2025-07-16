
import pygame
from const import *

class Draw:

    def draw_board(self, surface):
        for row in range(ROW):
            for col in range(COL):
                rect = (row * SQSIZE, col * SQSIZE, SQSIZE, SQSIZE)
                if (row + col) %2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                
                pygame.draw.rect(surface, color, rect)
