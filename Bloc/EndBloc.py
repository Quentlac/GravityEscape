from Item.Item2D import *
from Player import Player
import pygame

class EndBloc(Item2D):

    def __init__(self, pos, player, endcallback, material):
        super().__init__(pos, (50, 50))
        self.image_pos = (pos[0] - 25, pos[1] - 25)
        self.material = pygame.transform.scale(material, self._size)
        self.endcallback = endcallback
        self.player = player

    def testCollisionWithOtherItem(self, o, dx=0, dy=0):
        if isinstance(o, Player) and super().testCollisionWithOtherItem(o, dx, dy):
            self.endcallback()
            return False
        else:
            return super().testCollisionWithOtherItem(o, dx, dy)

    def display(self, canva, camera):
        self.testCollisionWithOtherItem(self.player)
        offset_x, offset_y = camera.getOffset()
        canva.blit(self.material, (offset_x + self.image_pos[0], offset_y + self.image_pos[1]))