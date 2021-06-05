import pygame
import random
from os import path
import sys 
sys.path.insert(1,'src/config')
sys.path.insert(1, 'src/assets')

from config import HEIGHT, WIDTH, FPS, game, world_speed, TELA_INICIAL, QUIT, GAME
from assets import load_assets
pygame.init()

def tela_inicial(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    tela_inicial = assets['telainicial']
    tela_inicial = pygame.transform.scale(tela_inicial, (WIDTH, HEIGHT))
    background_rect = tela_inicial.get_rect()

    estado = TELA_INICIAL
    while estado != GAME and estado != QUIT:
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                estado = GAME           

        screen.fill((0,0,0))
        screen.blit(tela_inicial, background_rect)

        pygame.display.update()

    return estado