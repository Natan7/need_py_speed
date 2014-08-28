# coding: utf-8

import pygame
from carro import *
from faixa import *
from pygame.locals import *


screen = pygame.display.get_surface()
tela = pygame.display.set_mode(####)
fundo = pygame.image.load('road3.png')

carro = Carro(screen)

faixa = Faixa(screen)







