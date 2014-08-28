import pygame
import random
from pygame.locals import *


class Arvores(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.arvores = ['tree.png', 'tree2.png', 'tree2.png', 'tree3.png', 'tree4.png', 'tree5.png']
        self.arvore_img = pygame.image.load(random.choice(self.arvores))
        self.tam_arvore_x = 20 
        self.tam_arvore_y = 20
        self.pos_arvore_x = 920
        self.pos_arvore_y = 455
    
    def muda_tam_arvore(self):
        self.tam_arvore_x += 10
        self.tam_arvore_y += 10
    
    def muda_pos_arvore(self):
        self.pos_arvore_x += 1* (self.tam_arvore_x / 6)
        self.pos_arvore_y += 1
        if self.pos_arvore_y > 1000:
            self.pos_arvore_y = 920
            self.pos_arvore_y = 455
            self.tam_arvore_x = 20
            self.tam_arvore_y = 20

    def print_arvore(self, screen):
        self.screen.blit(self.arvore_img, (self.pos_arvore_x, self.pos_arvore_y))

        
        

        
