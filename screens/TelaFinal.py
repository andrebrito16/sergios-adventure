import sys
from os import path
import pygame

# sys.path.insert(1, 'config')
# sys.path.insert(1, 'assets')

from utils.insert_paths import insert_paths_for_game

insert_paths_for_game()
img_dir = path.join(path.dirname(__file__), 'img')
BACKGROUND_IMG = 'background_img'
from config import HEIGHT, WIDTH, FPS, TELA_FINAL, QUIT, GAME
from assets import load_assets

pygame.init()
TELA = pygame.display.set_mode((WIDTH, HEIGHT))

player_speedy = 10

def tela_final(screen):
    assets = load_assets()

    tela_final = assets['telafinal']
    tela_final = pygame.transform.scale(tela_final, (WIDTH, HEIGHT))
    background_rect = tela_final.get_rect()
    
    clock = pygame.time.Clock()

    estado = TELA_FINAL
   
    while estado != QUIT and estado != GAME:
        
        clock.tick(FPS)

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            estado = QUIT
          elif event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
            estado = QUIT
          elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            estado = GAME


        screen.fill((255, 255, 255)) 
        screen.blit(tela_final, background_rect) 
        pygame.display.update()
    return estado