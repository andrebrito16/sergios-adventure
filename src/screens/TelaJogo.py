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

pygame.init()
TELA = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):

    def __init__(self, assets, posx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = 429
        self.rect.x = posx
        self.scale = 3
        self.assets = assets
       
    # Método update

all_sprites = pygame.sprite.Group()
def tela_jogo(screen):
    
    groups = {}
    groups['all_sprites'] = all_sprites
    assets = load_assets()

    all_sprites.add(Player(assets, 250))
    lista_sprites = [all_sprites]
    
    clock = pygame.time.Clock()

    
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
        
        all_sprites.update()
        all_sprites.draw(TELA)
        pygame.display.update()
        

        screen.fill((255, 255, 255))  # Preenche com a cor branca

     
    return estado