from Item.GravityItem import GravityItem
import pygame, os

class Player(GravityItem):

    # Répertoire contenant les images du personnage
    sprite_directory = "Sprites/walk"
    sprites_jump = "Sprites/jump"
    sprites_walk_back = "Sprites/walk_back"

    # Listes pour stocker les images du personnage pour chaque animation
    character_images_walk = []
    character_images_jump = []
    character_images_walk_back = []

    # Parcours les fichiers dans le répertoire "walk"
    for filename in os.listdir(sprite_directory):
        if filename.endswith(".png"):
            image = pygame.image.load(os.path.join(sprite_directory, filename))
            character_images_walk.append(image)

    # Parcours les fichiers dans le répertoire "jump"
    for filename in os.listdir(sprites_jump):
        if filename.endswith(".png"):
            image = pygame.image.load(os.path.join(sprites_jump, filename))
            character_images_jump.append(image)

    # Parcours les fichiers dans le répertoire "walk_back"
    for filename in os.listdir(sprites_walk_back):
        if filename.endswith(".png"):
            image = pygame.image.load(os.path.join(sprites_walk_back, filename))
            character_images_walk_back.append(image)

    def __init__(self, pos):
        super().__init__(pos, (20, 20), 0.02)
        self.current_frame = 0
        self._isPlayer = True
        self._isJump = False
        self.is_moving = False
        self.animation_delay = 10  # Délai entre les changements d'image
        self.animation_timer = 0  # Compteur pour contrôler l'animation
        self.current_animation = "idle"  # Animation par défaut
        self.idle_image = pygame.image.load(os.path.join("Sprites/walk", "walk1.png"))
        self.music = pygame.mixer.music
        self.walkingsound = False
        self.jumpsound = False


    def update_animation(self):
        # Choisissez l'animation appropriée en fonction de la situation
        if self.is_moving and self.is_front:
            self.current_animation = "walk"
            character_images = self.character_images_walk
            self.stopMoving()
        elif self.is_moving and self.is_back:
            self.current_animation = "walk_back"
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

    def display(self, canva):
        # Affiche l'image actuelle du personnage aux coordonnées (posX, posY)
        if self.current_animation == "idle":
            self.walkingsound = False
            self.jumpsound = False
            self.music.stop()
            canva.blit(self.idle_image, (self._posX, self._posY))
        elif self.current_animation in ["walk", "walk_back", "jump"]:
            character_images = getattr(self, f"character_images_{self.current_animation}")
            canva.blit(character_images[self.current_frame], (self._posX, self._posY))

        # Mettez à jour l'image actuelle (par exemple, pour l'animation)
        self.update_animation()

    def jump(self):
        if not self.jumpsound:
            self.music.load("ressources/sound-jump.mp3")
            self.music.play(1)
            print("Test")
            self.jumpsound = True
        if not self._isJump:
            self._isJump = True
            self.current_animation = "jump"  # Commencez l'animation de saut
            # Réinitialisez l'indice de l'image actuelle pour commencer par la première image de saut
            self.current_frame = 0

            self.addForce((0, -0.5))

    def goRight(self, dt):
        if not self.walkingsound:
            self.music.load("ressources/sound-moving.mp3")
            self.music.play(-1)
            self.walkingsound = True
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
        if not self.walkingsound:
            self.music.load("ressources/sound-moving.mp3")
            self.music.play(-1)
            self.walkingsound = True
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
