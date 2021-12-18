import pygame
class Sons:

    def musica_fundo(self):
        pygame.mixer.music.load('musics/fofolete_do_cao.mp3')
        pygame.mixer.music.play(-1)

    def barulho_colisao(self):
        pygame.mixer.Sound('musics/ganhar.wav')

    def lose_gasolina(self):
        pygame.mixer.Sound('musics/lose_gasolina.wav')
