import pygame


class Pause:

    def __init__(self, continue_cb, reset_cb, quit_cb):
        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)
        self.continue_cb = continue_cb
        self.reset_cb = reset_cb
        self.quit_cb = quit_cb
    def draw_text(self, text, font, color, window, x, y):
        # Création de l'objet
        textobj = font.render(text, 1, color)
        # On récupère le rectangle de l'objet
        textrect = textobj.get_rect()
        # On donne la position top left du rectangle
        textrect.center = (x, y)

        # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
        window.blit(textobj, textrect)

    def update(self, screen : pygame.Surface, events):
        screen.fill((200, 200, 200), screen.get_rect().inflate(-500, - 200))
        self.draw_text("Pause", self.font, "black", screen, screen.get_width() // 2, 150)

        # Créé les boutons
        button_1 = pygame.Rect(screen.get_size()[0] / 2 - 100, 220, 230, 100)
        button_2 = pygame.Rect(screen.get_size()[0] / 2 - 100, 360, 230, 100)
        button_3 = pygame.Rect(screen.get_size()[0] / 2 - 100, 500, 230, 100)

        # Créé les rectangles associés à chaque bouton
        pygame.draw.rect(screen, (231, 185, 0), button_1, border_radius=8)
        pygame.draw.rect(screen, (231, 185, 0), button_2, border_radius=8)
        pygame.draw.rect(screen, (231, 185, 0), button_3, border_radius=8)

        self.draw_text('Reprendre', self.font, "black", screen, button_1.centerx, button_1.centery)
        self.draw_text('Reset', self.font, "black", screen, button_2.centerx, button_2.centery)
        self.draw_text('Quitter', self.font, "black", screen, button_3.centerx, button_3.centery)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Récupère les positions x et y de la souris
                mx, my = pygame.mouse.get_pos()
                # Si on clique sur le bouton 1, lancement du jeu
                if button_1.collidepoint((mx, my)):
                    self.continue_cb()
                # SI on clique sur le bouton 2, crédits
                if button_2.collidepoint((mx, my)):
                    self.reset_cb()
                # Si on clique sur le bouton 3, on quitte le jeu
                if button_3.collidepoint((mx, my)):
                    self.quit_cb()