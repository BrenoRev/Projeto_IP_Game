import pygame

class Gasolina():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("images/gasolina.png"), (50, 50))