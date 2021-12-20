from pygame import QUIT, KEYDOWN, K_r
import time
from Start import *


class Hud:

    def start(self):
        startGame = Start()
        fonte2 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = f"Bateu!! Pressione a tecla R para continuar"
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()

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
        fonte3 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = f"VOCÊ PONTUOOU {pontos}, PARABÉNS"
        texto_formatado = fonte3.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        ret_texto.center = (512, 360)
        startGame.tela.blit(texto_formatado, ret_texto)
        pygame.display.update()
        time.sleep(10)

