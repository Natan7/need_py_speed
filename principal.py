# coding : utf-8

import pygame
from pygame import *
from faixa import *
from carro import *
from arvores import *

pygame.init()

tela =  pygame.display.set_mode((1600, 1000))
screen = pygame.display.get_surface()
fundo = pygame.image.load('road3.png')
pygame.display.set_caption('Need Py Speed - The Game')

clock = pygame.time.Clock()

carro = Carro(screen)
arvore = Arvores(screen)
lista_arvores = [arvore]
pygame.key.set_repeat(1,1)
i = 0

while True:
    clock.tick(60)

    if i % 100 == 0 and len(lista_arvores) < 20:
        lista_arvores.append(Arvores(screen))
    arvore.muda_tam_arvore()
    arvore.muda_pos_arvore()

    # Fechar o game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key.get_pressed()[K_ESCAPE]:    
            sys.exit()
    tecla = pygame.key.get_pressed()
    carro.mover_carro(tecla)
    tela.blit(fundo, (0, 0))
    carro.print_carro(screen)
    arvore.print_arvore(screen)
    pygame.display.update()        
     





