import pygame
from pygame.locals import *
from sys import exit
from random import randint
from Video import *
from Sons import *
from Nave import *
from Gasolina import *
from Meteoro import *

# Inicialização do jogo
pygame.mixer.init()
pygame.init()

# Icone da janela
icone = pygame.image.load("images/icon.jpg")
pygame.display.set_icon(icone)

# Nome da  tela
pygame.display.set_caption("A Viagem Espacial de Calegário")

# Tamanho da tela
largura = 1024
altura = 720

# Altura e largura da tela
tela = pygame.display.set_mode((largura, altura))

# Video
video = Video()
video.play()

# Sons
sons = Sons()
sons.musica_fundo()

# Nave
nave = Nave()

# Background
background = pygame.transform.scale(pygame.image.load("images/background.jpg"), (largura, altura))

# Gasolina
gasolina = Gasolina()
gasolina2 = Gasolina()
gasolina3 = Gasolina()


# Meteoro
meteoro = Meteoro(50,50)
meteoro2 = Meteoro(70,70)
meteoro3 = Meteoro(100,100)

# Pontuação inicial
pontuacao = 0

# Movimentação do jogador
x = largura/2
y = altura-100

# Quantidade de gasolina pega
get_gasolina = 0


# Quantidade de meteoros esquivados
noGet_meteoro = 0

# Relogio de tempo
relogio = pygame.time.Clock()

# Posição aleátoria gasolina 1
posicao_gasolinax = randint(0, largura - 40)
posicao_gasolinay = 0   #randint(0, altura - 40)

# Posição aleátoria gasolina 2
posicao_gasolinax2 = randint(0, largura - 40)
posicao_gasolinay2 = 0   #randint(0, altura - 40)

# Posição aleátoria gasolina 3
posicao_gasolinax3 = randint(0, largura - 40)
posicao_gasolinay3 = 0   #randint(0, altura - 40)

# Posição aleatória meteoro 1
posicao_meteorox = randint(0, largura - 40)
posicao_meteoroy = 0 #randint(0, largura - 40)

# Posição aleatória meteoro 2
posicao_meteorox2 = randint(0, largura - 70)
posicao_meteoroy2 = 0 #randint(0, largura - 40)

# Posição aleatória meteoro 3
posicao_meteorox3 = randint(0, largura - 100)
posicao_meteoroy3 = 0 #randint(0, largura - 40)

# Fonte das mensagens na telaa
fonte = pygame.font.SysFont("Arial", 30, True, True)

while True:
    # Carregar background
    tela.blit(background, (0, 0))

    # 30 segundos de tempo ao total
    tempo_total = (300000 / 1000)

    # Tirar 1 segundo a cada segundo
    tempo_total -= (pygame.time.get_ticks() / 1000)

    # FPS
    relogio.tick(60)

    # Se o tempo chegar até 0 perdeu
    if tempo_total <= 0:
        quit()

    # Fazer o meteoro e a gasolina descer
    posicao_gasolinay +=1
    posicao_meteoroy+= 1
    posicao_gasolinay2 +=1
    posicao_meteoroy2+=1.3
    posicao_gasolinay3+=1
    posicao_meteoroy3 += 1.6

    if get_gasolina >= 3:
        get_gasolina = 3

    # Aumentar a velocidade da gasolina toda vez que é pega
    posicao_gasolinay += get_gasolina
    posicao_gasolinay2 += get_gasolina
    posicao_gasolinay3 += get_gasolina


    # Mensagem na tela do tempo
    mensagem = f'Tempo: {int(tempo_total)}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    # Mensagem na tela da pontuação
    message = f'Pontuacao: {int(pontuacao)}'
    pontuacao_formatada = fonte.render(message, False, (255, 255, 255))

    for event in pygame.event.get():
        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Esquerda
        if pygame.key.get_pressed()[K_a]:
            if x <= 0:
                x += 30
            x -= 30
        # Direita
        if pygame.key.get_pressed()[K_d]:
            if x >= largura-100:
                x -= 30
            x += 30

            '''
        # Cima
        if pygame.key.get_pressed()[K_w]:
            if y <= 0:
                y += 10
            y -= 10
        # Baixo
        if pygame.key.get_pressed()[K_s]:
            if y >= altura-100:
                y -= 10
            y += 10
            '''

    # Fundo transparente pra o box não aparecer
    s = pygame.Surface((largura, altura))
    s.set_alpha(0)
    s.fill((255, 255, 255))

    # Colocar a nave e o fundo na tela
    tela.blit(s, (0, 0))
    tela.blit(nave.image, (x, y))

    # Criar um retângulo na nave para colidir
    ret_player = pygame.draw.rect(s, (0, 0, 0), (x, y, 100, 100))

    # Quadrado de colisão e imagem da gasolina
    ret_gasolina = pygame.draw.rect(s, (100, 100, 255), (posicao_gasolinax, posicao_gasolinay, 50, 50))
    tela.blit(gasolina.image, (posicao_gasolinax, posicao_gasolinay))

    ret_gasolina2 = pygame.draw.rect(s, (100, 100, 255), (posicao_gasolinax2, posicao_gasolinay2, 50, 50))
    tela.blit(gasolina2.image, (posicao_gasolinax2, posicao_gasolinay2))

    ret_gasolina3 = pygame.draw.rect(s, (100, 100, 255), (posicao_gasolinax3, posicao_gasolinay3, 50, 50))
    tela.blit(gasolina3.image, (posicao_gasolinax3, posicao_gasolinay3))

    # Criar um retângulo no meteoro para colidir
    ret_meteoro = pygame.draw.rect(s, (100, 100, 255), (posicao_meteorox, posicao_meteoroy, 50, 50))
    tela.blit(meteoro.image, (posicao_meteorox, posicao_meteoroy))

    ret_meteoro2 = pygame.draw.rect(s, (100, 100, 255), (posicao_meteorox2, posicao_meteoroy2, 70, 70))
    tela.blit(meteoro2.image, (posicao_meteorox2, posicao_meteoroy2))

    ret_meteoro3 = pygame.draw.rect(s, (100, 100, 255), (posicao_meteorox3, posicao_meteoroy3, 100, 100))
    tela.blit(meteoro3.image, (posicao_meteorox3, posicao_meteoroy3))

    # Colidir com a gasolina

    if ret_player.colliderect(ret_gasolina):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_gasolinax = randint(0, altura - 40)
        posicao_gasolinay = 0
        # Quando pegar a gasolina ganha + 50 pontos
        pontuacao += 50
        # Aumentar a velocidade da gasolina em 0.2
        get_gasolina+=0.2


    if ret_player.colliderect(ret_meteoro):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_meteorox = randint(0, largura - 40)
        posicao_meteoroy = randint(0, altura - 40)
        # Quando o meteoro bater na nave
        quit()

    if ret_player.colliderect(ret_gasolina2):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_gasolinax2 = randint(0, altura - 40)
        posicao_gasolinay2 = 0
        # Quando pegar a gasolina ganha + 50 pontos
        pontuacao += 50
        # Aumentar a velocidade da gasolina em 0.2
        get_gasolina += 0.2


    if ret_player.colliderect(ret_meteoro2):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_meteorox2 = randint(0, largura - 40)
        posicao_meteoroy2 = randint(0, altura - 40)
        # Quando o meteoro bater na nave
        quit()

    if ret_player.colliderect(ret_gasolina3):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_gasolinax3 = randint(0, altura - 40)
        posicao_gasolinay3 = 0
        # Quando pegar a gasolina ganha + 50 pontos
        pontuacao += 50
        # Aumentar a velocidade da gasolina em 0.2
        get_gasolina += 0.2

    if ret_player.colliderect(ret_meteoro3):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        posicao_meteorox3 = randint(0, largura - 40)
        posicao_meteoroy3 = randint(0, altura - 40)
        # Quando o meteoro bater na nave
        quit()

        # Se sair da tela voltar ao início
    if posicao_meteoroy >= altura-40:
        posicao_meteoroy = 0
        posicao_meteorox = randint(0, largura - 40)
    if posicao_gasolinay >= altura-40:
        lose_gasolina.play()
        posicao_gasolinay = 0
        posicao_gasolinax = randint(0, largura - 40)
        pontuacao -= (20 if pontuacao>=20 else 0)
    if posicao_meteoroy2 >= altura - 40:
        posicao_meteoroy2 = 0
        posicao_meteorox2 = randint(0, largura - 40)
    if posicao_gasolinay2 >= altura - 40:
       lose_gasolina.play()
       posicao_gasolinay2 = 0
       posicao_gasolinax2 = randint(0, largura - 40)
       pontuacao -= (20 if pontuacao>=20 else 0)
    if posicao_meteoroy3 >= altura - 40:
        posicao_meteoroy3 = 0
        posicao_meteorox3 = randint(0, largura - 40)
    if posicao_gasolinay3 >= altura - 40:
        lose_gasolina.play()
        posicao_gasolinay3 = 0
        posicao_gasolinax3 = randint(0, largura - 40)
        pontuacao -= (20 if pontuacao>=20 else 0)


    # Aparecer a pontuação e o tempo na tela
    tela.blit(pontuacao_formatada, (largura-300, 40))
    tela.blit(texto_formatado, (largura-200, 0))

        # Atualizar o jogo a cada iteração
    pygame.display.update()