import pygame as pg

class Camera:

    def __init__(self, level_width, level_height, x_start, y_start, screen: pg.Surface):
        self.camera_x = 0
        self.camera_y = 0
        self.level_width = level_width
        self.level_height = level_height
        self.size = 300
        self.half_size = self.size / 2
        (width, height) = screen.get_size()
        self.center_x = width/2
        self.center_y = height/2
        self.screen = screen
        offset = 20
        self.rect_screen = pg.Rect((offset, offset), (screen.get_size()[0] - offset * 2, screen.get_size()[1] - offset * 2))

    def update(self, player):
        rect = pg.Rect(self.center_x - self.half_size, self.center_y - self.half_size, self.size, self.size)

        pg.draw.rect(self.screen, (200,200,200), rect, 1)

        if not rect.collidepoint(player.getPosX(), player.getPosY()):
            if player.getPosX() < self.center_x - self.half_size:
                self.camera_x -= 20
            elif player.getPosX() > self.center_x + self.half_size:
                self.camera_x -= 20
            elif player.getPosY() < self.center_y - self.half_size:
                self.camera_y += 20
            elif player.getPosY() > self.center_y + self.half_size:
                self.camera_y -= 20

