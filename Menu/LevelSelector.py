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
        self.levels_locked = [level for level in self.levels if level[1].get("locked", True)]
        self.levels_unlocked = [level for level in self.levels if not level[1].get("locked", True)]
        self.completed = []
        self.reload_completed()
        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 40)

    def reload_completed(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + "/../completed.json", "r") as f:
            self.completed = json.load(f)

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

    def render_line(self, screen: pygame.Surface, dt, events, callback, return_cb, levels_list, height, y=0):
        space_witdh = 10
        card_width = 100
        total_width = card_width * len(levels_list) + space_witdh * (len(levels_list) - 1)
        start_x = screen.get_size()[0] / 2 - (total_width / 2)
        click_event = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_event = event
                events.remove(event)
        i = 0
        for (entry, level) in levels_list:
            rect = pygame.Rect(start_x + i * card_width + space_witdh * i, height, card_width, 100)
            pygame.draw.rect(screen, "darkgreen" if level.get("id", -1) in self.completed else "black", rect, 5)
            self.draw_text(str(y + 1), self.font, "black", screen, rect.centerx, rect.centery)
            if click_event:
                mx, my = pygame.mouse.get_pos()
                if rect.collidepoint(mx, my):
                    callback(entry)
            y += 1
            i += 1

        button_return = pygame.Rect(30, 30, 175, 50)
        pygame.draw.rect(screen, (0, 142, 114), button_return)
        self.draw_text('Return', self.font, "black", screen, button_return.centerx, button_return.centery + 7)
        if click_event:
            mx, my = pygame.mouse.get_pos()
            if button_return.collidepoint(mx, my):
                return_cb()
        return y

    def update(self, screen: pygame.Surface, dt, events, callback, return_cb):
        self.draw_text("Campagne", self.font, "black", screen, screen.get_size()[0] / 2, 160)
        l = len(self.levels_locked)
        if l > 0:
            i = self.render_line(screen, dt, events, callback, return_cb, self.levels_locked[0:min(l, 9)], 200)
        if l > 9:
            i = self.render_line(screen, dt, events, callback, return_cb, self.levels_locked[9:min(l, 17)], 310, i)
        if l > 17:
            self.render_line(screen, dt, events, callback, return_cb, self.levels_locked[18:min(l, 26)], 420, i)
        self.draw_text("Créatif", self.font, "black", screen, screen.get_size()[0] / 2, 560)
        self.render_line(screen, dt, events, callback, return_cb, self.levels_unlocked, 600)
