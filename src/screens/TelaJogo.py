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

class Barrel(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['barrel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1350
        self.rect.y = 380
        self.speedx  = -3
    
    def update(self):
        self.rect.x += self.speedx

class Player(pygame.sprite.Sprite):

    def __init__(self, assets, posx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = 429
        self.rect.x = posx
        self.scale = 3
       
    # Método update


all_sprites = pygame.sprite.Group()
all_barrels = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites 


def tela_jogo(screen):
    assets = load_assets()
    
    barrel1 = Barrel(assets)
    all_barrels.add(barrel1)
    

    all_sprites.add(Player(assets, 250))
    lista_sprites = [all_sprites]
    
    clock = pygame.time.Clock()

    
    background = assets['background']
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    estado = game
    barrel1.speedx
    while estado:
        clock.tick(FPS)
        if barrel1.rect.x < 400:
            barrel2 = Barrel(assets)

            all_barrels.add(barrel2)

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
        all_barrels.update()
        all_sprites.draw(TELA)
        all_barrels.draw(TELA)
        pygame.display.update()
        

        screen.fill((255, 255, 255))  # Preenche com a cor branca

     
    return estado