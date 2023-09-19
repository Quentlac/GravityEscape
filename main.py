import pygame
from Level import Level
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True

level = Level("level", screen)
dt = 0
while running:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    level.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()