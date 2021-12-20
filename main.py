from sys import exit
from pygame import *
from Background import *
from Gasolina import *
from Hud import *
from Meteoro import *
from Nave import *
from Sabredeluz import *
from Sons import *
from Video import *

# Inicialização do jogo
pygame.mixer.init()
pygame.init()

# Background
background = Background()

# Startar o jogo
startGame = Start()
surface = background.createSurface()

# Video
video = Video()
video.play()

# Sons
sons = Sons()
sons.musica_fundo()
pygame.mixer.music.play(-1)

# Nave
nave = Nave()

# Meteoros
meteoro = Meteoro(50)
meteoro2 = Meteoro(70)
meteoro3 = Meteoro(100)
# Gasolina
gasolina = Gasolina()
# Sabre de Luz
sabredeluz = Sabredeluz()

# Pontuação inicial
pontos = 0
pontosShow = 0

# Posição do spawn da nave
nave.position[0] = startGame.largura / 2
nave.position[1] = startGame.altura - 100

# Relogio de tempo
relogio = pygame.time.Clock()

# HUD
hud = Hud()

while True:
    # Carregar background
    startGame.tela.blit(background.image, (0, 0))

    # Carrega os objetos na tela
    nave.render(startGame.tela)

    meteoro.render(startGame.tela)
    meteoro2.render(startGame.tela)
    meteoro3.render(startGame.tela)

    gasolina.render(startGame.tela)

    sabredeluz.render(startGame.tela)

    # 360 segundos de tempo ao total
    tempo_total = 363

    # Tirar 1 segundo a cada segundo
    tempo_total -= (pygame.time.get_ticks() / 1000)

    # FPS
    relogio.tick(60)

    # Fazer a gasolina descer
    gasolina.moveGasolina()

    # Fazer o Sabre descer
    sabredeluz.movesabre()

    # Fazer o meteoro descer
    meteoro.moveMeteoro(1)
    meteoro2.moveMeteoro(1.3)
    meteoro3.moveMeteoro(1.6)

    # Mensagem na tela do tempo
    time = f'Tempo: {int(tempo_total)}'
    tempo = startGame.fonte.render(time, False, (255, 255, 255))

    # Mensagem na tela da pontuação
    points = f'Pontuacao: {int(pontos)}'
    pontuacao = startGame.fonte.render(points, False, (255, 255, 255))

    for event in pygame.event.get():
        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Esquerda
        if pygame.key.get_pressed()[K_a]:
            nave.move(-30)
        # Direita
        if pygame.key.get_pressed()[K_d]:
            nave.move(30)

    # Objetos de colisão
    colisao_meteoro = [meteoro.object(surface), meteoro2.object(surface), meteoro3.object(surface)]
    colisao_gasolina = gasolina.object(surface)
    colisao_sabre = sabredeluz.object(surface)
    nave_colide = nave.object(surface)
    startGame.tela.blit(surface, (0, 0))

    if nave_colide.colliderect(colisao_gasolina):
        pontos += 500
        pontosShow += 500
        sons.get_gasolina().play()
        gasolina.upVelocidade()
        gasolina.reset()

    if nave_colide.colliderect(colisao_sabre):
        sons.tocar_sabre().play()
        if pontos >= 100:
            pontosShow -= 100
            pontos -= 100
        sabredeluz.upVelocidade()
        sabredeluz.reset()

    if nave_colide.collidelistall(colisao_meteoro):
        sons.barulho_colisao().play()
        # Implementação da lógica da HUD
        if hud.start():
            gasolina.position()
            sabredeluz.reset()
            meteoro.resetar()
            meteoro2.resetar()
            meteoro3.resetar()
            pontos = 0
            tempo_total = 0

    if tempo_total <= 0:
        pygame.mixer.music.stop()
        hud.gameOver(pontosShow)
        break

    # Verifica se saiu da tela
    gasolina.outWindow()

    sabredeluz.outWindow()

    meteoro.outWindow()
    meteoro2.outWindow()
    meteoro3.outWindow()

    # Aparecer a pontuação e o tempo na tela
    startGame.tela.blit(pontuacao, (startGame.largura - 300, 40))
    startGame.tela.blit(tempo, (startGame.largura - 200, 0))

    # Atualizar o jogo a cada iteração
    pygame.display.flip()
