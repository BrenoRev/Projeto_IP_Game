import pygame
class Nave():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("images/sprite_nave.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.position = [0,0]

    def move(self, x=0):
        if self.position[0] <= 30:
            self.position[0]+=30
        if self.position[0] >= 924:
             self.position[0]-=30
        self.position[0] += x
        self.rect.centerx = self.position[0]

    def render(self, tela):
        tela.blit(self.image, (self.position[0], self.position[1]))

    def object(self, surface):
        return pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
