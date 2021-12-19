import pygame
from Start import *
from random import randint

class Gasolina():

    def __init__(self):
        self.largura = 720
        self.altura = 1024
        self.image = pygame.transform.scale(pygame.image.load("images/gasolina.png"), (50, 50))
        self.position()
        self.value = 1

    def moveGasolina(self):
        self.posicao_gasolinay+=self.value

    def upVelocidade(self):
        if self.value >= 3:
            self.value = 1.5
        self.value += 0.2

    def outWindow(self):
        if self.posicao_gasolinay >= self.altura - 40:
            self.position()

    def render(self, tela):
        tela.blit(self.image, (self.posicao_gasolinax, self.posicao_gasolinay))

    def object(self, surface):
        return pygame.draw.rect(surface, (255, 0, 0), (self.posicao_gasolinax, self.posicao_gasolinay, 50, 50))

    def reset(self):
        self.position()

    def position(self):
        self.posicao_gasolinax = randint(0, self.largura - 40)
        self.posicao_gasolinay = randint(0, 1000)*-1