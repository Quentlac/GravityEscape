import pygame
from pygame.locals import *
from Item.Item2D import Item2D
from Bloc.GravityBloc import *
from Bloc.StaticBloc import *
from Item.BulletItem import *
from Player import Player
from Level import Level

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Gravity Escape")

clock = pygame.time.Clock()
dt = 0

list_bloc = []

level = Level("level", window)

bullets = []



inGame = True

while inGame:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            inGame = False

    window.fill((100, 255, 255))
    pygame.mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)

    level.update(dt, events)

    pygame.display.update()

    dt = clock.tick(60)

pygame.quit()
