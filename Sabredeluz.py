import pygame
from Start import *
from random import randint

class Sabredeluz():

    def __init__(self):
        self.largura = 1080
        self.altura = 1536
        self.image = pygame.transform.scale(pygame.image.load("images/sabredeluz.png"), (50, 50))
        self.position()
        self.value = 1

    def movesabre(self):
        self.posicao_sabrey+=self.value

    def upVelocidade(self):
        if self.value >= 5:
            self.value = 2.0
        self.value += 0.4

    def outWindow(self):
        if self.posicao_sabrey >= self.altura - 40:
            self.position()

    def render(self, tela):
        tela.blit(self.image, (self.posicao_sabrex, self.posicao_sabrey))

    def object(self, surface):
        return pygame.draw.rect(surface, (255, 0, 0), (self.posicao_sabrex, self.posicao_sabrey, 50, 50))

    def reset(self):
        self.position()

    def position(self):
        self.posicao_sabrex = randint(0, self.largura - 40)
        self.posicao_sabrey = randint(0, 600) * -1