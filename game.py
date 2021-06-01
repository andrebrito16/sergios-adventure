
import sys
from os import path
import pygame
sys.path.insert(1, 'src/config')
sys.path.insert(1, 'src/screens')
from config import HEIGHT, WIDTH, FPS, game, world_speed, TELA_INICIAL, QUIT, GAME

from config import HEIGHT, WIDTH, FPS, game, world_speed
from src.screens.TelaInicio import tela_inicial
from src.screens.TelaJogo import tela_jogo

pygame.init()

#tela principal do jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')

estado = TELA_INICIAL

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        estado = tela_jogo(TELA)