import pygame
import sys
sys.path.insert(1, 'src/config')
from config import *
from os import path

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('src/assets/images/background.png').convert()
    return assets