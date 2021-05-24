import pygame
import sys
sys.path.insert(1, 'src/config')
from config import *
from os import path

def load_assets():  
    assets = {}
    player = pygame.image.load('src/assets/images/sergio.png').convert_alpha()
    assets['background'] = pygame.image.load('src/assets/images/background.png').convert()
    assets['player'] = pygame.transform.scale(player, (150, 150))
    barrel = pygame.image.load('src/assets/images/barril.png').convert_alpha()
    assets['barrel'] = pygame.transform.scale(barrel, (100, 100))
    return assets