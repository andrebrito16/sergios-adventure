import pygame
from config import *
import sys
from utils.setup_pygame import setup
sys.path.insert(1, 'config')

setup()

def load_assets():  
    assets = {}
    player_anim = []
    for i in range(4):
        filename = f'assets/images/sergio{i}.png'
        image = pygame.image.load(filename).convert_alpha()
        image = pygame.transform.scale(image, (87, 138))
        player_anim.append(image)
    assets['player'] = player_anim
    assets['background'] = pygame.image.load('assets/images/background.png').convert()
    barrel = pygame.image.load('assets/images/barril.png').convert_alpha()
    assets['barrel'] = pygame.transform.scale(barrel, (58, 98))
    assets["score_font"] = pygame.font.Font('assets/fonts/PressStart2P.ttf', 28)
    assets["telainicial"] = pygame.image.load('assets/images/tela_inicial.png').convert()   
    assets['telafinal'] = pygame.image.load('assets/images/tela_final.png').convert()
    assets['trilhasonora'] = pygame.mixer.Sound('assets/sounds/trilha.wav')
    assets['gameover'] = pygame.mixer.Sound('assets/sounds/gameover.wav')
    assets['barrelhit'] = pygame.mixer.Sound('assets/sounds/hit.wav')
    assets['jump'] = pygame.mixer.Sound('assets/sounds/jump.wav')
    sheep = pygame.image.load('assets/images/ovelha.png').convert_alpha()
    assets['sheep'] = pygame.transform.scale(sheep, (117, 108))
    return assets