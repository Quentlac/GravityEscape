import pygame


class LoreDisplayer:

    def __init__(self, text, done_cb):
        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 20)
        self.text = text + "\nPress enter to start level"
        self.index = 0
        self.dt_acc = 0
        self.done_cb = done_cb

    def update(self, screen: pygame.Surface, dt, events):
        self.dt_acc += dt
        if self.dt_acc > 30 and self.index < len(self.text):
            self.index += 1
            self.dt_acc = 0

        screen.fill((0, 0, 0))
        text = self.text[:self.index]
        words = text.split("\n")
        space = self.font.size(' ')[0]
        max_width, max_height = screen.get_size()
        pos = (screen.get_size()[0] / 4, screen.get_size()[1] / 2 - 30)
        x, y = pos
        for line in words:
            word_height = 0
            for word in line:
                word_surface = self.font.render(word, True, (200, 200, 200))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

        for event in events:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN):
                if self.index < len(self.text):
                    self.index = len(self.text)
                else:
                    self.done_cb()

