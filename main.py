import pygame
from pygame.locals import *
from Bloc.GravityBloc import *
from Level import Level

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Gravity Escape")

clock = pygame.time.Clock()
dt = 0

level = Level("level", window)



inGame = True

while inGame:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            inGame = False

    window.fill((0, 0, 0))

    level.update(dt)

    pygame.display.update()

    dt = clock.tick(60)

pygame.quit()
