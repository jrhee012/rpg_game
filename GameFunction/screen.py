import pygame
from enum import Enum
import logging
import __root__
import os
# from .settings import Settings
# from .states import StateValue

logger = logging.getLogger("MAIN")
default_name = "RPG"
root_dir = __root__.path()
# active_screen: list = []


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file: str = "", location: list = (0, 0)):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        print('sss', self)
        pygame.display.flip()


class UpdateSetting(Enum):
    BG_IMAGE: str = "BG_IMAGE"
    SCREEN_WIDTH: str = "SCREEN_WIDTH"


class Screen:
    def __init__(self, settings, name: str = default_name):
        self.name = "Main Screen - %s" % name
        self.settings = None
        self.background = None
        self.state = None
        self.screen = None

        self.main(settings, name)

    def main(self, settings, name: str = default_name) -> None:
        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.RESIZABLE)
        screen.fill(settings.background_colour)
        # print('sscren ', screen)
        pygame.display.set_caption(name)
        self.screen = screen
        self.settings = settings

    def update_background_img(self, image_file: str = "", location: list = (0, 0)) -> None:
        print("Background!")
        print("bg img @ %s" % image_file)
        background = Background(image_file, location)

    def update_state(self, state) -> None:
        print("update state!")
        bg_img_path: str = os.path.join(root_dir, "data", "img")
        bg_img_path += "/" + str(state.name.value) + ".png"
        # bg_img_path += "/" + "ghost.png"
        # print('dffdfd', bg_img_path)
        self.set_background(bg_img_path, [0, 0])

    def set_background(self, img_path, location):
        # new_background = Background(img_path, location)
        # print('nb: ', new_background, self.screen)
        # self.background = new_background
        # self.screen.blit(pygame.image.load(img_path), [100, 100])
        self.screen.fill([0, 0, 0])
        pygame.display.flip()
