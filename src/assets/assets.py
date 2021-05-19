import pygame
import sys
sys.path.insert(1, 'src/config')
from config import *
from os import path

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('src/assets/images/samplebackground.png').convert()
    return assets