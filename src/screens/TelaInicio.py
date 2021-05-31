import pygame
import random
from os import path
import sys 
sys.path.insert(1,'src/config')

from config import FPS

def tela_inicio(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    estado = TELA_INICIO
    while estado != GAME and estado != QUIT:
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                estado = GAME           

        screen.fill((0,0,0))

        pygame.display.flip()

    return estado