import pygame
class Nave():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("images/sprite_nave.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100
        self.position = [0,0]

    def update(self, x, y):
        self.position[0] += x
        self.position[1] += y
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]