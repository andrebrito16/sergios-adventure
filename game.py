import sys
from os import path
import pygame

sys.path.insert(1, 'src/config')
sys.path.insert(1, 'src/screens')

from config import HEIGHT, WIDTH, FPS, world_speed, GAME, QUIT, TELA_FINAL
from src.screens.TelaJogo import tela_jogo
from src.screens.TelaFinal import tela_final

pygame.init()
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')

estado = GAME

while estado != QUIT:
    if estado == GAME:
        estado = tela_jogo(TELA, 3)
    if estado == TELA_FINAL:
        estado = tela_final(TELA)

pygame.quit()