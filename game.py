import sys
from os import path
import pygame

sys.path.insert(1, 'src/config')
sys.path.insert(1, 'src/screens')

from config import HEIGHT, WIDTH, FPS, game, world_speed
from src.screens.TelaJogo import tela_jogo

pygame.init()
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sérgio e as Ovelhas Radioativas')

try:
    tela_jogo(TELA)
finally:
    pygame.quit() 