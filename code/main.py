
import pygame 
import sys 

from const import *
from draw import Draw
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')

        self.draw = Draw()
        self.game = self.draw.game
        self.board = self.draw.game.board


    def GameStart(self):

        while True:

            self.draw.draw_board(self.screen)
            self.draw.draw_piece(self.screen, self.board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = int(y // SQSIZE)
                    col = int(x // SQSIZE)

                    if self.game.square_click == (row, col):
                        self.game.square_click = ()
                        self.game.click = []
                    else:
                        self.game.square_click = (row, col)
                        self.game.click.append(self.game.square_click)
                    
                    if len(self.game.click) == 2:
                        move = Move(self.game.click[0], self.game.click[1], self.board)
                        print(move.move_loca(self.game.click[0], self.game.click[1]))

                        if move in self.game.valid_moves:
                            self.game.make_move(move)
                            self.game.valid_moves = self.game.get_possible_move()
                        
                        self.game.square_click = ()
                        self.game.click = []
                            
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.game.undo_move()

            pygame.display.update()


main = Main()
main.GameStart()