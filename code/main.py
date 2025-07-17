
import pygame 
import sys 

from const import *
from draw import Draw
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')

        self.draw = Draw()
        self.game = Game()
        self.board = self.game.board


    def GameStart(self):

        while True:

            self.draw.draw_board(self.screen)
            self.draw.draw_piece(self.screen, self.board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.GameStart()