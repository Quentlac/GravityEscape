import pygame
from pygame.locals import *
from Item2D import Item2D
from GravityItem import GravityItem
from Player import Player

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Gravity Escape")

floor = GravityItem((500, 700), (1000, 100), 0)
roof = GravityItem((500, 0), (1000, 100), 0)

list_bloc = []

def shoot(x, y):

    s = Item2D((x, y), (5, 5))

    for b in list_bloc:
        if(b.testCollisionWithOtherItem(s)):
            print("Invert", b)
            b.invertGravity()
            return True

    return False

inGame = True

player = Player((200, 200))

while inGame:
    for event in pygame.event.get():
        if event.type == QUIT:
            inGame = False
        if event.type == MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            if not shoot(posX, posY):
                list_bloc.append(GravityItem((posX, posY), (50, 50), 0.0002))

    window.fill((0, 0, 0))

    floor.display(window)
    roof.display(window)

    for b in list_bloc:
        b.display(window)
        b.move()

    player.display(window)
    player.move()

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if(keys[K_SPACE]):
        player.jump()

    if(keys[K_RIGHT]):
        player.goRight()

    if(keys[K_LEFT]):
        player.goLeft()

pygame.quit()
