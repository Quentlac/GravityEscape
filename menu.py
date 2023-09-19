import pygame
import sys

# Démarrage de l'horloge
clock = pygame.time.Clock()

# Initialisation de pygame et déclaration de variables
pygame.init()
res = (1024,768)
white = (255,255,255)
black = (0,0,0)
font = pygame.font.SysFont("arial", 32)
click = False

# Création de la fenêtre
screen = pygame.display.set_mode(res)


def draw_text(text, font, color, window, x, y):
    surfaceObject = font.render(text, 1, color)
    textrect = surfaceObject.get_rect()
    textrect.topleft = (x,y)
    """
    print("Width")
    print(textrect.width)
    print("Height")
    print(textrect.height)
    """
    window.blit(surfaceObject, textrect)


def start_menu():
    while True:
        screen.fill(white)
        draw_text("Gravity Escape", font, black, screen, screen.get_width()//2-104,40)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(screen.get_width()//2-100, 200, 200, 100)
        button_2 = pygame.Rect(screen.get_width()//2-100, 350, 200, 100)

        if button_1.collidepoint((mx,my)):
            if click:
                game()

        if button_2.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255,0,0), button_1)
        pygame.draw.rect(screen, (255,0,0), button_2)

        draw_text('Start', font, black, screen, screen.get_width()//2-33, button_1.bottom-button_1.height//2-16)
        draw_text('Exit', font, black, screen, screen.get_width()//2-25, button_2.bottom-button_2.height//2-16)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        clock.tick(60)


def game():
    running = True
    while running:
        screen.fill(black)
        draw_text('GAME SCREEN', font, white, screen, 20,20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)



start_menu()
