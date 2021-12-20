import pygame
from Start import *
from random import randint

class Meteoro:
    def __init__(self, size):
        self.altura = 720
        self.largura = 1024

        self.image = pygame.transform.scale(pygame.image.load("images/foto_meteoro1.png"), (size, size))

        self.posicao_meteorox = randint(0, self.largura - 40)
        self.posicao_meteoroy = 0

        self.size = size

    def moveMeteoro(self, value):
            self.posicao_meteoroy+= value

    def outWindow(self):
        if self.posicao_meteoroy >= self.altura - self.size:
            self.posicao_meteoroy = 0
            self.posicao_meteorox = randint(0, self.largura - 40)

    def render(self, tela,):
        tela.blit(self.image, (self.posicao_meteorox, self.posicao_meteoroy))

    def object(self, surface):
        return pygame.draw.rect(surface, (255, 0, 0), (self.posicao_meteorox, self.posicao_meteoroy, self.size, self.size))

    def resetar(self):
        self.posicao_meteorox = randint(0, self.largura - 40)
        self.posicao_meteoroy = 0