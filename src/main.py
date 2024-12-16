import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))

from menu.menu import Menu
from level_1.level1 import Level1

clock = pygame.time.Clock()

menu = Menu(screen=screen, levels=[
    Level1(screen=screen)
    # add more levels here
])

while True:
    menu.inputs()

    menu.graphics()

    pygame.display.flip()
    clock.tick(60)
