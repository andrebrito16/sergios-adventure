
import sys
from os import path
import pygame
sys.path.insert(1, 'config')
sys.path.insert(1, 'screens')
sys.path.insert(1, 'assets')
from config import HEIGHT, WIDTH, FPS, game, world_speed, TELA_INICIAL, QUIT, GAME, TELA_FINAL
from screens.TelaInicio import tela_inicial
from screens.TelaJogo import tela_jogo
from screens.TelaFinal import tela_final


pygame.init()
pygame.mixer.init()

#tela principal do jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')

estado = TELA_INICIAL

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        estado = tela_jogo(TELA, 3)
    if estado == TELA_FINAL:
        estado = tela_final(TELA)

pygame.quit()
