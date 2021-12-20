from pygame import QUIT, KEYDOWN, K_r, K_x
import time
from Start import *


class Hud:

    def inicio(self):
        startGame = Start()
        fonte2 = pygame.font.SysFont('arial', 40, True, True)
        mensagem = f"BEM VINDO! PRESSIONE X PARA INICIAR"
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()

        startGame.tela.blit(startGame.image, (0, 0))
        startGame.tela.blit(startGame.calegario, (0, 200))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_x:
                        return False
            ret_texto.center = (512, 360)
            startGame.tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    def start(self):
        startGame = Start()
        fonte2 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = f"Bateu!! Pressione a tecla R para continuar"
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        startGame.tela.blit(startGame.image, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        return True
            ret_texto.center = (512, 360)
            startGame.tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    def gameOver(self, pontos):
        startGame = Start()
<<<<<<< HEAD
        fonte3 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = f"VOCÊ PONTUOU {pontos}, PARABÉNS"
=======
        fonte3 = pygame.font.SysFont('arial', 40, True, True)
        mensagem = f"VOCÊ PONTUOU {pontos} PONTOS, PARABÉNS!"
>>>>>>> 55348b9b1ec3b259ac4e08f4254188b52b961aa8
        texto_formatado = fonte3.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        ret_texto.center = (512, 360)
        startGame.tela.blit(startGame.image, (0, 0))
        startGame.tela.blit(texto_formatado, ret_texto)
        pygame.display.update()
        time.sleep(10)

