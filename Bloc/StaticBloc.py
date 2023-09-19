from Item.GravityItem import GravityItem
import pygame as pg


class StaticBloc(GravityItem):

    def __init__(self, pos, size, material, is_solid=True):
        super().__init__(pos, size, 0, is_solid=is_solid)
        self.image_pos = (pos[0] - size[0] / 2, pos[1] - size[1] / 2)
        self.material = pg.transform.scale(material, self._size)

    def display(self, canva, camera):
        offset_x, offset_y = camera.getOffset()

        canva.blit(self.material, (offset_x +self.image_pos[0], offset_y + self.image_pos[1]))
