import pygame

class Meteoro:
    def __init__(self,x,y):
        self.image = pygame.transform.scale(pygame.image.load("images/foto_meteoro1.png"), (x, y))