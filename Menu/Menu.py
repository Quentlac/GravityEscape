import pygame
import math
from Menu.LevelSelector import LevelSelector

# Made by Guillaume, adapted into class by Nathan
class Menu:
    SELECT = 1
    CREDIT = 2
    LEVELS = 3

    def __init__(self, screen):
        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)
        self.font_return = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 20)
        self.background = pygame.image.load("view/background/background-menu-large.png").convert()
        self.background.set_alpha(220)
        self.limit = math.ceil(screen.get_width() / self.background.get_width()) + 1
        self.scroll = 0
        self.current = Menu.SELECT
        self.screen = screen
        self.levels_selector = LevelSelector()
        self.init_music()

    def init_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("ressources/Iron_Maiden_-_Fear_Of_The_Dark.mp3")
        pygame.mixer.music.play(-1)

    def draw_text(self, text, font, color, window, x, y):
        # Création de l'objet
        textObj = font.render(text, 1, color)
        # On récupère le rectangle de l'objet
        textrect = textObj.get_rect()
        # On donne la position top left du rectangle
        textrect.topleft = (x, y)
        """""
        print("Width")
        print(textrect.width)
        print("Height")
        print(textrect.height)
        """""
        # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
        window.blit(textObj, textrect)

    def home(self):
        self.current = Menu.SELECT
    def update(self, events, game):
        i = 0
        while i < self.limit:
            self.screen.blit(self.background, (self.background.get_width() * i + self.scroll, 0))
            i += 1
        # Gérer la vitesse du background (1 = plus lent)
        self.scroll -= 3
        # Permet de refaire boucler le scroll à 0 pour recommencer la boucle au dessus
        if abs(self.scroll) > self.background.get_width():
            self.scroll = 0

        if self.current == Menu.SELECT:
            self.render_select(events, game)
        elif self.current == Menu.CREDIT:
            self.render_credit(events)
        elif self.current == Menu.LEVELS:
            self.levels_selector.update(self.screen, 0, events, game.set_game, self.home)

    def render_select(self, events, game):
        # Dessine le titre du jeu
        self.draw_text("Gravity Escape", self.font, "black", self.screen, self.screen.get_width() // 2 - 148, 40)

        # Créé les boutons
        button_1 = pygame.Rect(self.screen.get_width() // 2 - 100, 200, 200, 100)
        button_2 = pygame.Rect(self.screen.get_width() // 2 - 100, 350, 200, 100)
        button_3 = pygame.Rect(self.screen.get_width() // 2 - 100, 500, 200, 100)

        # Créé les rectangles associés à chaque bouton
        pygame.draw.rect(self.screen, (0, 142, 114), button_1)
        pygame.draw.rect(self.screen, (0, 142, 114), button_2)
        pygame.draw.rect(self.screen, (0, 142, 114), button_3)

        # Génère le texte à l'intérieur de chaque bouton, les coordonées sont gérées manuellement
        self.draw_text('Start', self.font, "black", self.screen, self.screen.get_width() // 2 - 55,
                       button_1.bottom - button_1.height // 2 - 16)
        self.draw_text('Credits', self.font, "black", self.screen, self.screen.get_width() // 2 - 73,
                       button_2.bottom - button_2.height // 2 - 16)
        self.draw_text('Exit', self.font, "black", self.screen, self.screen.get_width() // 2 - 38,
                       button_3.bottom - button_3.height // 2 - 16)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Récupère les positions x et y de la souris
                mx, my = pygame.mouse.get_pos()
                # Si on clique sur le bouton 1, lancement du jeu
                if button_1.collidepoint((mx, my)):
                    self.current = Menu.LEVELS

                # SI on clique sur le bouton 2, crédits
                if button_2.collidepoint((mx, my)):
                    self.current = Menu.CREDIT

                # Si on clique sur le bouton 3, on quitte le jeu
                if button_3.collidepoint((mx, my)):
                    pygame.quit()
                events.remove(event)
    def render_credit(self, events):
        button_return = pygame.Rect(30, 30, 100, 50)
        pygame.draw.rect(self.screen, (0, 142, 114), button_return)
        self.draw_text('Return', self.font_return, "black", self.screen, button_return.width // 2 - 5,
                       button_return.bottom - button_return.height // 2 - 7)

        # Titre crédit et crédits en dessous
        self.draw_text("CREDITS", self.font, "black", self.screen, self.screen.get_width() // 2 - 71, 40)
        self.draw_text("-X (pour le truc)", self.font, "black", self.screen, self.screen.get_width() // 2 - 161, 150)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.current = Menu.SELECT
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Récupère les positions x et y de la souris
                mx, my = pygame.mouse.get_pos()
                # Si on clique sur le bouton 1, lancement du jeu
                if button_return.collidepoint((mx, my)):
                    self.current = Menu.SELECT
                events.remove(event)
