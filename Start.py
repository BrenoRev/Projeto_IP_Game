import pygame

class Start:

    def __init__(self):
        self.icone = pygame.image.load("images/icon.jpg")
        pygame.display.set_icon(self.icone)

        # Nome da  tela
        pygame.display.set_caption("A Viagem Espacial de Calegário")

        # Tamanho da tela
        self.largura = 1024
        self.altura = 720

        # Altura e largura da tela
        self.tela = pygame.display.set_mode((self.largura, self.altura))

        self.fonte = pygame.font.SysFont("Arial", 30, True, True)

        self.image = pygame.transform.scale(pygame.image.load("images/background.jpg"),(1024, 720))
        # redimensionar para 400x400
        self.calegario = pygame.transform.scale(pygame.image.load("images/calegario.png"),(400, 400)).convert_alpha()