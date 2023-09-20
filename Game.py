import pygame

from LoreDisplayer import LoreDisplayer
from Menu.Menu import Menu


class Game:
    MENU = 1
    GAME = 2

    isRunning = True

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Gravity Escape")

        self.current = Game.MENU

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.menu = Menu(self.screen)
        self.game = None

    def change_dispay(self, page):
        self.current = page

    def set_game(self):
        self.game = LoreDisplayer("ksdjsqidjsdlksd sq|\ndlksqjdsddjjsqfkls fsjf lksjlkjqlsqf")
        self.current = Game.GAME
    def run(self):

        while Game.isRunning:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    Game.isRunning = False
                    break

            self.screen.fill((0, 0, 0))
            #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

            if self.current == Game.MENU:
                self.menu.update(events, self)
            if self.current == Game.GAME and self.game:
                self.game.update(self.screen, self.dt, events)

            pygame.display.update()

            self.dt = self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
