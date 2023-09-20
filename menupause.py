import pygame
import sys
import math

# Démarrage de l'horloge
clock = pygame.time.Clock()

# Initialisation de pygame et déclaration de variables
pygame.init()
res = (1024, 768)
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)
click = False

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Pause")


def draw_text(text, font, color, window, x, y):
    # Création de l'objet
    textobj = font.render(text, 1, color)
    # On récupère le rectangle de l'objet
    textrect = textobj.get_rect()
    # On donne la position top left du rectangle
    textrect.topleft = (x, y)

    print("Width")
    print(textrect.width)
    print("Height")
    print(textrect.height)

    # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
    window.blit(textobj, textrect)


def start_menu():
    while True:
        screen.fill(white)
        # Dessine le titre du jeu
        draw_text("Pause", font, black, screen, screen.get_width() // 2 - 57, 40)

        # Créé les boutons
        button_1 = pygame.Rect(250, 350, 200, 100)
        button_2 = pygame.Rect(574, 350, 200, 100)

        # Créé les rectangles associés à chaque bouton
        pygame.draw.rect(screen, (0, 142, 114), button_1)
        pygame.draw.rect(screen, (0, 142, 114), button_2)

        # Génère le texte à l'intérieur de chaque bouton, les coordonées sont gérées manuellement
        draw_text('Continue', font, black, screen, (button_1.left + button_1.right) // 2 - 90,
                  button_1.bottom - button_1.height // 2 - 16)
        draw_text('Quit', font, black, screen, (button_2.left + button_2.right) // 2 - 43,
                  button_2.bottom - button_2.height // 2 - 16)

        # Récupère les positions x et y de la souris
        mx, my = pygame.mouse.get_pos()
        # Si on clique sur le bouton 1, lancement du jeu
        if button_1.collidepoint((mx, my)):
            if click:
                print("test")

        # SI on clique sur le bouton 2, crédits
        if button_2.collidepoint((mx, my)):
            if click:
                print("test2")

        # Si pas de clique, une boucle détecte les sorties du jeu via les boutons de fermeture
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        if button_2.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


start_menu()
