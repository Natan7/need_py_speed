import pygame
from pygame.locals import *

class Faixa(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.img_faixa = pygame.image.load('faixa.png')
        self.largura = 11
        self.altura = 15
        self.pos_x = 790
        self.pos_y = 455
    
    def muda_pos(self):
        self.pos_x -= 0.6
        self.pos_y += 0.5 * (self.altura / 10)

    def muda_tam_faixa(self,aum_largura ,aum_altura ):
        self.imagem_red = self.img_faixa
        self.imagem_red = pygame.transform.scale(self.img_faixa, ((self.largura + aum_largura), (self.altura + aum_altura)))
        self.altura += 7
        self.largura += 2
    def print_faixa(self):
        self.screen.blit( pygame.image.load('faixa.png'), (790, 455))
        


