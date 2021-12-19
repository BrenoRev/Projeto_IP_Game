import pygame
class Sons:

    def musica_fundo(self):
        return pygame.mixer.music.load('musics/fofolete_do_cao.mp3')

    def barulho_colisao(self):
        return pygame.mixer.Sound('musics/colisao.wav')

    def lose_gasolina(self):
        return pygame.mixer.Sound('musics/lose_gasolina.wav')

    def get_gasolina(self):
        return pygame.mixer.Sound('musics/ganhar.wav')
