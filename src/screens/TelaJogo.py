import sys
from os import path
import pygame

sys.path.insert(1, 'src/config')
sys.path.insert(1, 'src/assets')
img_dir = path.join(path.dirname(__file__), 'img')
print(img_dir)
BACKGROUND_IMG = 'background_img'
from config import HEIGHT, WIDTH, FPS, game, world_speed
from assets import load_assets



def tela_jogo(screen):
    clock = pygame.time.Clock()

    assets = load_assets()
    background = assets['background']
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    estado = game

    while estado:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = False

        
        background_rect.x += world_speed
        if background_rect.right < 0:
            background_rect.x += background_rect.width

        screen.blit(background, background_rect)

        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        pygame.display.flip()
    

        screen.fill((255, 255, 255))  # Preenche com a cor branca

     
    return estado