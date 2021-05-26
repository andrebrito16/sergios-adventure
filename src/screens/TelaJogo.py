import sys
import random
from time import sleep
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
        self.speedx  = -(random.randint(6, 8))

    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x < -100:
            self.kill()

        

GROUND = HEIGHT * 5//6 - 30
GRAVITY = 1.2
JUMP_SIZE = 30
STILL = 0
JUMPING = 1
FALLING = 2
class Player(pygame.sprite.Sprite):

    def __init__(self, assets, posx):
        pygame.sprite.Sprite.__init__(self)

        self.player = assets['player']
        self.frame = 0
        self.image = self.player[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = 429
        self.rect.x = posx
        self.state = STILL
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 20
        self.speedy = 0
       
    # Método update
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um quadro.
            self.frame += 1

            if self.frame == len(self.player):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.player[self.frame]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.center = center

        self.speedy += GRAVITY

        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy

        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL
        
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING



all_sprites = pygame.sprite.Group()
all_barrels = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites 

player_speedy = 10
def tela_jogo(screen):
    lives = 3
    assets = load_assets()
    
    barrel_last = Barrel(assets)
    all_barrels.add(barrel_last)
    
    player = Player(assets, 250)
    all_sprites.add(player)
    lista_sprites = [all_sprites]
    
    clock = pygame.time.Clock()

    background = assets['background']
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    estado = game

    while estado:
        clock.tick(FPS)
        if barrel_last.rect.x < 1325-400 and random.randint(1,100) == 2: 
            barrel_last = Barrel(assets)
            barrel_last.speedx = -(random.randint(6, 8))
            all_barrels.add(barrel_last)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        background_rect.x += world_speed
        if background_rect.right < 0:
            background_rect.x += background_rect.width

        screen.blit(background, background_rect)

        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        hits = pygame.sprite.spritecollide(player, all_barrels, True)

        if len(hits) > 0:
            lives -= 1
        if lives == 0:
            estado = False

        # hits_barrel = pygame.sprite.spritecollide(barrel_last, all_barrels, True)
       
            
        
        
        all_sprites.update()
        all_barrels.update()
        all_sprites.draw(TELA)
        all_barrels.draw(TELA)
        pygame.display.update()
        

        screen.fill((255, 255, 255))  # Preenche com a cor branca

     
    return estado