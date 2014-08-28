import pygame
from pygame.locals import *
pygame.init()
import os

class Faixa(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.img_faixa = pygame.image.load('faixa.png')
        self.largura = 11
        self.altura = 15
        self.pos_x = 790
        self.pos_y = 470 
    
    def muda_pos_faixa(self):
        self.pos_x -= 0.6
        self.pos_y += 0.5 * (self.altura / 10)
        if self.pos_y > 1000:
            self.pos_x = 790
            self.pos_y = 470
            self.largura = 11
            self.altura = 15

    def muda_tam_faixa(self):
        self.altura += 7 
        self.largura += 2
    def print_faixa(self, screen):
        self.arvore_print = pygame.transform.scale(self.img_faixa,(self.largura, self.altura))
        self.screen.blit(self.arvore_print, (self.pos_x, self.pos_y))
        


