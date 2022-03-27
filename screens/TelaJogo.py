import random
from os import path
import pygame
from utils.insert_paths import insert_paths_for_game
from utils.setup_pygame import setup
insert_paths_for_game()
from assets import load_assets
from config import FPS, GAME, HEIGHT, QUIT, TELA_FINAL, WIDTH, world_speed

setup()

TELA = pygame.display.set_mode((WIDTH, HEIGHT))

class Barrel(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['barrel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 1350
        self.rect.y = 380
        self.speedx  = -(6)

    
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
       
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
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

class Sheep(pygame.sprite.Sprite):
    def __init__(self, assets, posx):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['sheep']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = 429
        self.rect.x = posx

    def update(self):
        self.rect.centery = (random.randint(429, 439))

all_sheep = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_barrels = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites 

def tela_jogo(screen, lives):
    assets = load_assets()
    
    pygame.mixer.music.load('assets/sounds/trilha.wav')
    pygame.mixer.music.set_volume(0.4)

    pygame.mixer.music.play(loops = -1)
    score = 0
    
    for counter in range(5):
        sheep = Sheep(assets, counter*20)
        all_sheep.add(sheep)

    barrel_last = Barrel(assets)
    all_barrels.add(barrel_last)
    
    player = Player(assets, 250)
    all_sprites.add(player)
    
    clock = pygame.time.Clock()

    background = assets['background']
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    estado = GAME
    pygame.mixer.music.play(loops=-1)
    while estado != TELA_FINAL and estado != QUIT:
        score += 1
        clock.tick(FPS)
        if barrel_last.rect.x < 1325-400 and random.randint(1,100) == 2: 
            barrel_last = Barrel(assets)
            barrel_last.speedx = -(6+score*0.0025)
            all_barrels.add(barrel_last)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    assets['jump'].play()
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
            assets['barrelhit'].play()
            lives -= 1
        if lives == 0:
            assets['gameover'].play()
            estado = TELA_FINAL
            player.kill()
        if score % 1000 == 0:
            lives += 1
       
        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        TELA.blit(text_surface, text_rect)

        text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        TELA.blit(text_surface, text_rect)
        
        all_sheep.update()
        all_sprites.update()
        all_barrels.update()
        all_sprites.draw(TELA)
        all_barrels.draw(TELA)
        all_sheep.draw(TELA)
        pygame.display.update()
    
        screen.fill((255, 255, 255))  

    return estado
