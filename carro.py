import pygame

class Carro(pygame.sprite.Sprite):
    def __init__ (self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.img_carro = pygame.image.load('car.png')
        self.rect_carro = self.img_carro.get_rect()
        self.pos_carro_x = 500 
        self.pos_carro_y = 600

    def mover_carro(self, tecla):
        if tecla[pygame.K_LEFT] and self.pos_carro_x > -100 :
            self.pos_carro_x -= 20 
        elif tecla[pygame.K_RIGHT] and self.pos_carro_x < 1100:  
            self.pos_carro_x += 20

    
            
    def print_carro(self, screen):
        self.screen.blit(self.img_carro, (self.pos_carro_x, self.pos_carro_y))
        
       
 
 
