import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define a largura e altura da janela
largura = 800
altura = 600

# Cria a tela com a dimensão especificada
tela = pygame.display.set_mode((largura, altura))

# Definição de cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Posição e parâmetros do círculo
x = largura // 2
y = altura // 2
raio = 20
velocidade = 5

# Cor de fundo
cor_fundo = (0, 0, 0)

# Loop principal do jogo
while True:
    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenha o círculo na tela
    pygame.draw.circle(tela, azul, (x, y), raio)

    # Verifica os eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura o estado das teclas
    teclas = pygame.key.get_pressed()

    # Movimenta o círculo de acordo com as teclas pressionadas
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros (60 FPS)
    pygame.time.Clock().tick(60)
