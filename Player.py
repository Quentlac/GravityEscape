import math

from Item.GravityItem import GravityItem
import pygame, os


class Player(GravityItem):
    size = (25, 45)
    img_size = (50, 50)
    # Répertoire contenant les images du personnage
    sprite_directory = os.path.dirname(os.path.realpath(__file__)) + "/Sprites/walk"
    sprites_jump = os.path.dirname(os.path.realpath(__file__)) + "/Sprites/jump"
    sprites_walk_back = os.path.dirname(os.path.realpath(__file__)) + "/Sprites/walk_back"

    # Listes pour stocker les images du personnage pour chaque animation
    character_images_walk = []
    character_images_jump = []
    character_images_walk_back = []

    @staticmethod
    def load_image(array, img_dir, size):
        for filename in os.listdir(img_dir):
            if filename.endswith(".png"):
                image = pygame.image.load(os.path.join(img_dir, filename))
                image = pygame.transform.scale(image, size)
                array.append(image)

    def __init__(self, pos):
        super().__init__(pos, self.size, 0.001)
        self.current_frame = 0
        self._isPlayer = True
        self._isJump = False
        self.is_moving = False
        self.animation_delay = 10  # Délai entre les changements d'image
        self.animation_timer = 0  # Compteur pour contrôler l'animation
        self.current_animation = "idle"  # Animation par défaut
        self.idle_image = pygame.transform.scale(pygame.image.load(os.path.join("Sprites/walk", "walk1.png")),
                                                 self.img_size)
        self.idle_image_back = pygame.transform.scale(pygame.image.load(os.path.join("Sprites/walk_back", "walk_back1"
                                                                                                          ".png")),
                                                      self.img_size)
        self.last_direction_forward = True
        gunImg = pygame.image.load(os.path.join("view/", "gunpistol.png"))
        self.gunImgRight = pygame.transform.scale(gunImg, (50, 20))
        self.gunImgLeft = pygame.transform.flip(self.gunImgRight, False, True)

    def update_animation(self):
        # Choisissez l'animation appropriée en fonction de la situation
        if self.is_moving and self.is_front:
            self.current_animation = "walk"
            character_images = self.character_images_walk
            self.last_direction_forward = True
            self.stopMoving()
        elif self.is_moving and self.is_back:
            self.current_animation = "walk_back"
            self.last_direction_forward = False
            character_images = self.character_images_walk_back
            self.stopMoving()
        elif self._isJump:
            self.current_animation = "jump"
            character_images = self.character_images_jump
        else:
            self.current_animation = "idle"  # Par défaut, pour l'animation inactif
            character_images = None  # Ajoutez cette ligne pour déclarer character_images

        # Mettez à jour l'image actuelle en fonction de l'animation
        if character_images:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_delay:
                self.current_frame = (self.current_frame + 1) % len(character_images)
                self.animation_timer = 0

    def display(self, canva, camera):
        # Remove comment to see hitbox
        #pygame.draw.rect(canva, 'red', pygame.Rect(camera.getOffset()[0] + self._posX - self._width / 2,camera.getOffset()[1] + self._posY - self._height / 2, self._width, self._height), 1)
        # Affiche l'image actuelle du personnage aux coordonnées (posX, posY)
        offset_x, offset_y = camera.getOffset()
        pos = (offset_x + self._posX - self.idle_image.get_size()[0] / 2,offset_y + self._posY - self.idle_image.get_size()[1] / 2)

        shotgun = pygame.surface.Surface((60, 60), pygame.SRCALPHA)
        shotgun.fill((0, 0, 0, 0))

        #pygame.draw.rect(shotgun, 'darkblue', (25, 25, 20, 6))
        if(-offset_x + pygame.mouse.get_pos()[0] > self.getPosX()):
            shotgun.blit(self.gunImgRight, (10, 30))
        else:
            shotgun.blit(self.gunImgLeft, (10, 10))

        angle = math.atan2((-offset_y + pygame.mouse.get_pos()[1] - self.getPosY()), (-offset_x + pygame.mouse.get_pos()[0] - self.getPosX()))

        shotgun_r = rot_center(shotgun,  -angle/math.pi * 180)

        canva.blit(shotgun_r, (offset_x + self._posX - 30, offset_y + self._posY - 35))

        if self.current_animation == "idle":
            if self.last_direction_forward:
                canva.blit(self.idle_image, pos)
            else:
                canva.blit(self.idle_image_back, pos)
        elif self.current_animation in ["walk", "walk_back", "jump"]:
            try:
                character_images = getattr(self, f"character_images_{self.current_animation}")
                canva.blit(character_images[self.current_frame], pos)
            except IndexError as e:
                print("Frame error: ", e)
                canva.blit(self.idle_image, pos)

        # Mettez à jour l'image actuelle (par exemple, pour l'animation)
        self.update_animation()

    def jump(self, dt):
        if (not self._isJump):
            self._isJump = True
            self.addForce((0, -0.45))
            self.current_animation = "jump"  # Commencez l'animation de saut

            # Réinitialisez l'indice de l'image actuelle pour commencer par la première image de saut
            self.current_frame = 0

    def goRight(self, dt):
        nextX = self.getPosX() + 0.15 * dt
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)
        self.is_front = True  # Le joueur se déplace en avant
        self.is_moving = True
        self.isJump = False
        self.is_back = False

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX - 0.15 * dt, nextY)

    def goLeft(self, dt):
        nextX = self.getPosX() - 0.15 * dt
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)
        self.is_moving = True
        self.is_back = True  # Le joueur se déplace en arrière
        self.isJump = False
        self.is_front = False

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX + 0.15 * dt, nextY)

    def stopMoving(self):
        self.is_moving = False

    def is_dead(self, height):
        if self.getPosY() > height + 100:
            return True
        for b in GravityItem.getItems():
            if (b != self and math.sqrt((self._posX - b._posX)**2 + (self._posY - b._posY)**2) < 25 ):
                return True
        return False

Player.load_image(Player.character_images_walk, Player.sprite_directory, Player.img_size)
Player.load_image(Player.character_images_jump, Player.sprites_jump, Player.img_size)
Player.load_image(Player.character_images_walk_back, Player.sprites_walk_back, Player.img_size)

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
