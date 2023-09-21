import json
import os

import pygame


class LevelSelector:

    def __init__(self):
        self.levels = []
        basepath = os.path.dirname(os.path.realpath(__file__)) + "/../Levels/"
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                if ".json" in entry:
                    with open(os.path.join(basepath, entry), "r") as f:
                        json_data = json.load(f)
                        json_data['grid'] = None
                        self.levels.append((entry, json_data))
        self.levels = sorted(self.levels, key=lambda d: d[1]['id'])
        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)

    def draw_text(self, text, font, color, window, x, y):
        # Création de l'objet
        textObj = font.render(text, 1, color)
        # On récupère le rectangle de l'objet
        textrect = textObj.get_rect()
        # On donne la position top left du rectangle
        textrect.center = (x, y)
        """""
        print("Width")
        print(textrect.width)
        print("Height")
        print(textrect.height)
        """""
        # Dessine l'objet surface dans son rectangle sur la window passée en paramètre
        window.blit(textObj, textrect)
    def update(self, screen: pygame.Surface, dt, events, callback, return_cb):
        space_witdh = 50
        card_width = 100
        total_width = card_width * len(self.levels) + space_witdh * (len(self.levels) - 1)
        start_x = screen.get_size()[0] / 2 - (total_width / 2)
        click_event = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                click_event = event
        for i, (entry, level) in enumerate(self.levels):
            rect = pygame.Rect(start_x + i * card_width + space_witdh * i, 300, card_width, 200)
            pygame.draw.rect(screen, "black", rect, 5)
            self.draw_text(str(i + 1), self.font, "black", screen, rect.centerx, rect.centery)
            if click_event:
                mx, my = pygame.mouse.get_pos()
                if rect.collidepoint(mx, my):
                    callback(entry)

        button_return = pygame.Rect(30, 30, 175, 50)
        pygame.draw.rect(screen, (0, 142, 114), button_return)
        self.draw_text('Return', self.font, "black", screen, button_return.centerx, button_return.centery + 7)
        if click_event:
            mx, my = pygame.mouse.get_pos()
            if button_return.collidepoint(mx, my):
                return_cb()
