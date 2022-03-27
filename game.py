import pygame
from utils.insert_paths import insert_paths_for_game
insert_paths_for_game()
from utils.setup_pygame import setup
from config import HEIGHT, WIDTH, TELA_INICIAL, QUIT, GAME, TELA_FINAL
from screens.TelaInicio import tela_inicial
from screens.TelaJogo import tela_jogo
from screens.TelaFinal import tela_final

setup()

TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sérgio's Adventure: Escape from Cumbria")

estado = TELA_INICIAL

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        estado = tela_jogo(TELA, 3)
    if estado == TELA_FINAL:
        estado = tela_final(TELA)

pygame.quit()
