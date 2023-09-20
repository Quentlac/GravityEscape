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
font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)
font_return = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 20)
click = False
scroll = 0
music = pygame.mixer.music.load("ressources/Iron_Maiden_-_Fear_Of_The_Dark.mp3")


# Création de la fenêtre
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Gravity Escape")

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
    """""
    print("Width")
    print(textrect.width)
    print("Height")
    print(textrect.height)
    """""
    # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
    window.blit(textObj, textrect)


# Fonction de génération du menu
def start_menu():
    while True:
        # Variable globale scroll pour faire défiler le background
        global scroll

        screen.fill(white)
        # Boucle de défilement du background de 0 à 2 non-inclus, cela permet de répéter le background à l'infini
        i = 0
        while (i<limit):
            screen.blit(background, (background.get_width()*i+scroll,0))
            i += 1
        # Gérer la vitesse du background (1 = plus lent)
        scroll -= 3
        # Permet de refaire boucler le scroll à 0 pour recommencer la boucle au dessus
        if abs(scroll) > background.get_width():
            scroll = 0

        # Dessine le titre du jeu
        draw_text("Gravity Escape", font, black, screen, screen.get_width()//2-148,40)

        # Créé les boutons
        button_1 = pygame.Rect(screen.get_width()//2-100, 200, 200, 100)
        button_2 = pygame.Rect(screen.get_width()//2-100, 350, 200, 100)
        button_3 = pygame.Rect(screen.get_width()//2-100, 500, 200, 100)

        # Créé les rectangles associés à chaque bouton
        pygame.draw.rect(screen, (0, 142, 114), button_1)
        pygame.draw.rect(screen, (0, 142, 114), button_2)
        pygame.draw.rect(screen, (0, 142, 114), button_3)

        # Génère le texte à l'intérieur de chaque bouton, les coordonées sont gérées manuellement
        draw_text('Start', font, black, screen, screen.get_width() // 2 - 55,
                  button_1.bottom - button_1.height // 2 - 16)
        draw_text('Credits', font, black, screen, screen.get_width() // 2 - 73,
                  button_2.bottom - button_2.height // 2 - 16)
        draw_text('Exit', font, black, screen, screen.get_width() // 2 - 38,
                  button_3.bottom - button_3.height // 2 - 16)


        # Récupère les positions x et y de la souris
        mx, my = pygame.mouse.get_pos()
        # Si on clique sur le bouton 1, lancement du jeu
        if button_1.collidepoint((mx,my)):
            if click:
                game()

        # SI on clique sur le bouton 2, crédits
        if button_2.collidepoint((mx,my)):
            if click:
                credits()

        # Si on clique sur le bouton 3, on quitte le jeu
        if button_3.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()

        # Si pas de clique, une boucle détecte les sorties du jeu via les boutons de fermeture
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


# Fonction à changer quand intégration de toutes les branches
def game():
    # Boucle qui lance le jeu
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

def credits():
    # On laisse le background défiler
    running = True
    global click
    while running:
        global scroll
        screen.fill(white)
        # Boucle de défilement du background de 0 à 2 non-inclus, cela permet de répéter le background à l'infini
        i = 0
        while (i < limit):
            screen.blit(background, (background.get_width() * i + scroll, 0))
            i += 1
        # Gérer la vitesse du background (1 = plus lent)
        scroll -= 3
        # Permet de refaire boucler le scroll à 0 pour recommencer la boucle au dessus
        if abs(scroll) > background.get_width():
            scroll = 0

        button_return = pygame.Rect(30, 30, 100, 50)
        pygame.draw.rect(screen, (0, 142, 114), button_return)
        draw_text('Return', font_return, black, screen, button_return.width // 2 - 5,
                  button_return.bottom - button_return.height // 2 - 7)

        # Titre crédit et crédits en dessous
        draw_text("CREDITS", font, black, screen, screen.get_width()//2-71,40)
        draw_text("-X (pour le truc)", font, black, screen, screen.get_width()//2-161,150)

        # Lors d'un appui sur echap, retourne vers le menu principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            mx, my = pygame.mouse.get_pos()
            if button_return.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


start_menu()
