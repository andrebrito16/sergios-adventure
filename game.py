
import sys
from os import path
import pygame


sys.path.insert(1, 'src/config')
sys.path.insert(1, 'src/screens')

from config import HEIGHT, WIDTH, FPS, game, world_speed
from src.screens.TelaInicio import tela_inicio
from src.screens.TelaJogo import tela_jogo

pygame.init()

#tela principal do jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')

#estado = INIT
#while estado != QUIT:
    #if estado == INIT:
        #estado = tela_inicio(window)
    #elif estado == GAME:
        #estado = tela_jogo(window)
    #else:
        #state = QUIT

try:
    tela_inicio(TELA)
finally:
    pygame.quit()