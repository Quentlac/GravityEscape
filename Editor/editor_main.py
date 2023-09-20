import pygame
from Editor.Editor import Editor
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

editor = Editor(screen)

dt = 0
while running:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    editor.update(events, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()
