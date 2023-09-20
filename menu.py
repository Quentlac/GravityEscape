import pygame
import sys
import math

# Démarrage de l'horloge
clock = pygame.time.Clock()

# Initialisation de pygame et déclaration de variables
pygame.init()
res = (1024,768)
white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 32)
click = False
scroll = 0


# Création de la fenêtre
screen = pygame.display.set_mode(res)

# Load l'image de background, descendre son opacité, et limite (ici 2) de répétition de l'image de fond pour éviter les lags
background = pygame.image.load("view/background/background-menu-large.png").convert()
background.set_alpha(220)
limit = math.ceil(screen.get_width()/background.get_width()) + 1


def draw_text(text, font, color, window, x, y):
    # Création de l'objet
    textObj = font.render(text, 1, color)
    # On récupère le rectangle de l'objet
    textrect = textObj.get_rect()
    # On donne la position top left du rectangle
    textrect.topleft = (x,y)
    """
    print("Width")
    print(textrect.width)
    print("Height")
    print(textrect.height)
    """
    # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
    window.blit(textObj, textrect)


def start_menu():
    while True:
        global scroll
        screen.fill(white)
        i = 0
        while (i<limit):
            screen.blit(background, (background.get_width()*i+scroll,0))
            i += 1

        scroll -= 3
        if abs(scroll) > background.get_width():
            scroll = 0


        draw_text("Gravity Escape", font, black, screen, screen.get_width()//2-117,40)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(screen.get_width()//2-100, 250, 200, 100)
        button_2 = pygame.Rect(screen.get_width()//2-100, 450, 200, 100)

        if button_1.collidepoint((mx,my)):
            if click:
                game()

        if button_2.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (0,142,114), button_1)
        pygame.draw.rect(screen, (0,142,114), button_2)

        draw_text('Start', font, black, screen, screen.get_width()//2-44, button_1.bottom-button_1.height//2-16)
        draw_text('Exit', font, black, screen, screen.get_width()//2-30, button_2.bottom-button_2.height//2-16)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
