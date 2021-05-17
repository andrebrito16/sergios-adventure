import sys
import pygame

sys.path.insert(1, 'src/config')

from config import HEIGH, WIDTH, FPS, game

# Gera a tela do jogo
pygame.init()
TELA = pygame.display.set_mode((WIDTH, HEIGH))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')


# Rotina do ícone
estado = game

while estado:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            estado = False

    # ----- Gera saídas
    TELA.fill((255, 255, 255))  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
