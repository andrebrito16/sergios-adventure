import pygame
import sys
sys.path.insert(1, 'src/config')
from config import *
from os import path

def load_assets():  
    assets = {}
    player_anim = []
    for i in range(4):
        filename = f'src/assets/images/sergio{i}.png'
        image = pygame.image.load(filename).convert_alpha()
        image = pygame.transform.scale(image, (87, 138))
        player_anim.append(image)
    assets['player'] = player_anim

    # player = pygame.image.load('src/assets/images/sergio.png').convert_alpha()
    assets['background'] = pygame.image.load('src/assets/images/background.png').convert()
    # assets['player'] = pygame.transform.scale(player, (150, 150))
    barrel = pygame.image.load('src/assets/images/barril.png').convert_alpha()
    assets['barrel'] = pygame.transform.scale(barrel, (58, 98))
    assets["score_font"] = pygame.font.Font('src/assets/fonts/PressStart2P.ttf', 28)
    assets['telafinal'] = pygame.image.load('src/assets/images/tela_final.png').convert()
    return assets