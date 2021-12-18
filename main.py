from pygame import *
from sys import exit
from Video import *
from Sons import *
from Nave import *
from Gasolina import *
from Meteoro import *
from Start import *
from Background import *

# Inicialização do jogo
pygame.mixer.init()
pygame.init()

# Startar o jogo
startGame = Start()

# Video
video = Video()
video.play()

# Sons
sons = Sons()
sons.musica_fundo()

# Nave
nave = Nave()

# Background
background = Background()

# Gasolina
gasolina = Gasolina()
gasolina2 = Gasolina()
gasolina3 = Gasolina()

# Meteoro
meteoro = Meteoro(50)
meteoro2 = Meteoro(70)
meteoro3 = Meteoro(100)

# Pontuação inicial
pontos = 0

# Posição do spawn da nave
nave.position[0] = startGame.largura/2
nave.position[1] = startGame.altura-100

# Relogio de tempo
relogio = pygame.time.Clock()

while True:
    # Carregar background
    startGame.tela.blit(background.image, (0, 0))

    # Carrega os objetos na tela

    nave.render(startGame.tela)

    gasolina.render(startGame.tela)
    gasolina2.render(startGame.tela)
    gasolina3.render(startGame.tela)

    meteoro.render(startGame.tela)
    meteoro2.render(startGame.tela)
    meteoro3.render(startGame.tela)

    # 30 segundos de tempo ao total
    tempo_total = (300)

    # Tirar 1 segundo a cada segundo
    tempo_total -= (pygame.time.get_ticks()/1000)

    # FPS
    relogio.tick(60)

    # Se o tempo chegar até 0, perdeu
    if tempo_total <= 0:
        quit()

    # Fazer a gasolina descer
    gasolina.moveGasolina()
    gasolina2.moveGasolina()
    gasolina3.moveGasolina()

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

    # Verifica se saiu da tela
    gasolina.outWindow()
    gasolina2.outWindow()
    gasolina3.outWindow()

    meteoro.outWindow()
    meteoro2.outWindow()
    meteoro3.outWindow()

    # Aparecer a pontuação e o tempo na tela
    startGame.tela.blit(pontuacao, (startGame.largura-300, 40))
    startGame.tela.blit(tempo, (startGame.largura-200, 0))

    # Atualizar o jogo a cada iteração
    pygame.display.flip()