
import pygame 
import sys 

from const import *
from draw import Draw

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')

        self.draw = Draw()


    def GameStart(self):
        
        draw = self.draw
        screen = self.screen

        while True:

            draw.draw_board(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.GameStart()