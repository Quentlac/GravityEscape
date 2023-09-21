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
        # Charge le logo du jeu
        title_image = pygame.image.load("view/gravity-logo.png")
        title_rect = title_image.get_rect()

        # Redimensionne le logo de 70%
        new_width = int(title_rect.width * 0.6)
        new_height = int(title_rect.height * 0.6)
        title_image = pygame.transform.scale(title_image, (new_width, new_height))
        title_rect = title_image.get_rect()

        # On positionne le logo au bon endroit
        title_rect.center = (self.screen.get_width() // 2, 100)

        # On affiche le logo sur l'écran
        self.screen.blit(title_image, title_rect)

        # Créé les boutons
        button_1 = pygame.Rect(self.screen.get_width() // 2 - 110, 200, 220, 100)
        button_2 = pygame.Rect(self.screen.get_width() // 2 - 110, 350, 220, 100)
        button_3 = pygame.Rect(self.screen.get_width() // 2 - 110, 500, 220, 100)

        # Dessine les bordures noires autour des rectangles jaunes
        border_width = 2  # Largeur de la bordure
        pygame.draw.rect(self.screen, (231, 185, 0), button_1, border_radius=8)
        pygame.draw.rect(self.screen, (231, 185, 0), button_2, border_radius=8)
        pygame.draw.rect(self.screen, (231, 185, 0), button_3, border_radius=8)

        # Génère le texte à l'intérieur de chaque bouton, les coordonées sont gérées manuellement
        self.draw_text('DEMARRER', self.font, "black", self.screen, self.screen.get_width() // 2 - 90,
                       button_1.bottom - button_1.height // 2 - 16)
        self.draw_text('CREDITS', self.font, "black", self.screen, self.screen.get_width() // 2 - 73,
                       button_2.bottom - button_2.height // 2 - 16)
        self.draw_text('QUITTER', self.font, "black", self.screen, self.screen.get_width() // 2 - 75,
                       button_3.bottom - button_3.height // 2 - 16)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.remove(event)
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

    def render_credit(self, events):
        button_return = pygame.Rect(30, 30, 100, 50)
        pygame.draw.rect(self.screen, (231, 185, 0), button_return, border_radius=8)
        self.draw_text('Retour', self.font_return, "black", self.screen, button_return.width // 2 - 5, button_return.bottom - button_return.height // 2 - 7)

        # Titre crédit et crédits en dessous
        self.draw_text("CREDITS", self.font, "black", self.screen, self.screen.get_width() // 2 - 70, 40)



        self.draw_text("Sprites & Decors :", self.font, "black", self.screen, self.screen.get_width() // 2 - 475, 130)
        self.draw_text("- Pack de blocs : @analogstudios_", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 180)
        self.draw_text("- Artwork Robot : Amon - OpenGameArt", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 210)
        self.draw_text("- DECOR : ClassicBackground - Freepik", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 240)


        self.draw_text("Musiques :", self.font, "black", self.screen, self.screen.get_width() // 2 - 475, 280)
        self.draw_text("- Fear of The Dark, Iron Maiden (but SM64)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 330)
        self.draw_text("- Come as You Are, Nirvana (but SM64)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 360)
        self.draw_text("- Bad Guy, Billie Eilish (but SM64)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 390)
        self.draw_text("- The Epic 2, Rafael Kruz", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 420)

        self.draw_text("Equipe :", self.font, "black", self.screen, self.screen.get_width() // 2 - 475, 470)
        self.draw_text("- Guillaume Perrin, chef de projet (Orga de l'équipe, lore du jeu & création des menus)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 520)
        self.draw_text("- Timeo Cogne, graphisme & animations (Animation des Sprites/Textures/Musiques)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 550)
        self.draw_text("- Quentin Lacombe, développeur (Physique du jeu)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 580)
        self.draw_text("- Nathan Guillermo, développeur (Structure du jeu et des niveaux)", self.font_return, "black", self.screen, self.screen.get_width() // 2 - 375, 610)



        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.current = Menu.SELECT
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.remove(event)
                # Récupère les positions x et y de la souris
                mx, my = pygame.mouse.get_pos()
                # Si on clique sur le bouton 1, lancement du jeu
                if button_return.collidepoint((mx, my)):
                    self.current = Menu.SELECT

