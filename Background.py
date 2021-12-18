import pygame

class Background():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("images/background.jpg"),(1024, 720))

    def createSurface(self):
        surface = pygame.Surface((1080, 720))
        surface.set_alpha(0)
        surface.fill((255, 255, 255))
        return surface