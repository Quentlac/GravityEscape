class Camera:
    def __init__(self, player, size):
        self.camera_x = 0
        self.camera_y = 0

        self.camera_target_x = 0
        self.camera_target_y = 0

        self.camera_width = size[0]
        self.camera_height = size[1]

        self._player = player
        self._speed = 0.01

    def move(self, dt):
        self.camera_target_x = self._player.getPosX()

        self.camera_target_y = self._player.getPosY()

        self.camera_x += (self.camera_target_x - self.camera_x) * self._speed * dt
        self.camera_y += (self.camera_target_y - self.camera_y) * self._speed * dt




    def getOffset(self):
        return (-(self.camera_x - self.camera_width / 2), -(self.camera_y - self.camera_height / 2))

    def getParralaxOffset(self, qp):
        return (-(self.camera_x - self.camera_width / 2)*qp, -(self.camera_y - self.camera_height / 2)*qp)


