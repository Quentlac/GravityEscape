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

floor = GravityItem((500, 700), (1000, 100))
roof = GravityItem((500, 0), (1000, 100))

list_bloc = []

level = Level("level", window)

bullets = []

def shoot(x, y):
    dx = x - player.getPosX()
    dy = y - player.getPosY()

    visee = pygame.Vector2(dx, dy)
    visee = visee.normalize()

    bullets.append(BulletItem((player.getPosX(), player.getPosY()), (visee.x, visee.y)))

inGame = True

player = Player((200, 200))

while inGame:
    for event in pygame.event.get():
        if event.type == QUIT:
            inGame = False
        if event.type == MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            shoot(posX, posY)

    window.fill((0, 0, 0))
    pygame.mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)

    floor.display(window)
    roof.display(window)

    level.update(dt)

    for b in list_bloc:
        b.display(window)
        b.move(dt)

    for b in bullets:
        b.display(window)
        b.move(dt)

        if not b.active:
            bullets.remove(b)

    player.display(window)
    player.move(dt)

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if(keys[K_SPACE]):
        player.jump()

    if(keys[K_d] or keys[K_RIGHT]):
        player.goRight(dt)

    if(keys[K_q] or keys[K_LEFT]):
        player.goLeft(dt)

    dt = clock.tick(60)

pygame.quit()
