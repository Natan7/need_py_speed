import pygame, sys
from pygame import *
pygame.init()
import os
from faixa import Faixa 

clock = pygame.time.Clock()

# Matriz arvore = [[arvore, [dim], [pos]]]
# Background
tam_tela = largura, altura = (1600, 1000) 
tela = pygame.display.set_mode(tam_tela)
background = pygame.image.load('road3.png')

# Carro 
carro = pygame.image.load('car.png')

# Faixa 

faixa = pygame.image.load('faixa.png')
faixa2 = faixa
dim_faixa = [11, 15]
faixa_red = pygame.transform.scale(faixa, dim_faixa)
pos_faixa = [790, 470] 

# Arvores direita

dim_arvores = [20, 20]
arvored = pygame.image.load('tree.png')
pos1_arvore = [920, 455]

# Arvores esquerda

arvoree = pygame.image.load('tree2.png')
pos2_arvore = [680, 455]

pygame.key.set_repeat(1,1)

# Inserindo Backgrond na tela

tela.blit(imagem, (0,0))
tela.blit(faixa, pos_faixa) 
pygame.display.update()

pos_carro = [500, 600]
velocidade = 0
voltas = 0
velocidade = 01 
i = 0


faixa = Faixa()

while True:

    clock.tick(60)
    # Fechar o game
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_carro[0] -= 4 
            elif event.key == pygame.K_RIGHT:
                pos_carro[0] += 4
            elif event.key == pygame.K_UP:
                dim_arvores[0] += 10 
                dim_arvores[1] += 10 
                pos1_arvore[0] += 1 * (dim_arvores[0] / 6) 
                pos1_arvore[1] += 0.1
                pos2_arvore[0] -= 1 * (dim_arvores[0] / 4)
                pos2_arvore[1] += 1 
                pos_faixa[0] -= 0.6 
                pos_faixa[1] += 0.5 * (dim_faixa[1] / 10) 
                dim_faixa[0] += 2 
                dim_faixa[1] += 7 
                velocidade += 0.1


		

        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key.get_pressed()[K_ESCAPE]:
            sys.exit()
         
    
    faixa_red = pygame.transform.scale(faixa, dim_faixa)
    arvored_red = pygame.transform.scale(arvored, dim_arvores)
    arvoree_red = pygame.transform.scale(arvoree, dim_arvores)
    tela.fill((0, 0, 0))
    tela.blit(imagem, (0,0))
    tela.blit(faixa_red, pos_faixa) 
    tela.blit(arvored_red,pos1_arvore)        
    tela.blit(arvoree_red, pos2_arvore)
    tela.blit(carro, pos_carro) 
    pygame.display.update()
    
    i += 1
    if pos1_arvore[0] > 1600:
        pos1_arvore = [925, 455]    
        dim_arvores = [20, 20]
        pos2_arvore = [680, 455]
 
    if pos_faixa[1] > 850:
        pos_faixa = [790, 470]
        dim_faixa = [11, 15]
         
