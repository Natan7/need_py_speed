import pygame
import random
from pygame.locals import *


class Arvores(pygame.sprite.Sprite):
    def __init__(self, screen,lado):
        pygame.sprite.Sprite.__init__(self)
        if lado == 'direita':
            self.pos_arvore_x = 920
            self.pos_arvore_y = 455
        elif lado == 'esquerda':
            self.pos_arvore_x = 650
            self.pos_arvore_y = 455
            
        self.screen = screen
        self.arvores = ['tree.png', 'tree2.png', 'tree2.png', 'tree3.png', 'tree4.png', 'tree5.png']
        self.arvore_img = pygame.image.load(random.choice(self.arvores))
        self.tam_arvore_x = 20 
        self.tam_arvore_y = 20

    def muda_pos_arvore(self, lado):
        if lado == 'direita':
            self.pos_arvore_x += 1  * (self.tam_arvore_x / 6) 
        elif lado == 'esquerda':
            self.pos_arvore_x -= 2 * (self.tam_arvore_x / 6)
        self.pos_arvore_y += 0.1 

        if self.pos_arvore_x > 1600 and lado == 'direita':
            self.pos_arvore_x= 920
            self.pos_arvore_y = 455
            self.tam_arvore_x = 20
            self.tam_arvore_y = 20

        elif self.pos_arvore_x < -250 and lado == 'esquerda':
            self.pos_arvore_x = 650
            self.pos_arvore_y = 455
            self.tam_arvore_x = 20
            self.tam_arvore_y = 20


    
    def muda_tam_arvore(self):  
        self.tam_arvore_x += 10 
        self.tam_arvore_y += 10 

    def print_arvore(self, screen):
        self.arvore_print = pygame.transform.scale(self.arvore_img, (self.tam_arvore_x, self.tam_arvore_y))
        self.screen.blit(self.arvore_print, (self.pos_arvore_x, self.pos_arvore_y))

        
        

        
