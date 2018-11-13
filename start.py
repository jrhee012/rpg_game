import pygame
from GameFunction import settings, keys


def main():

    pygame.init()

    init_settings = settings.Settings()
    init_settings.check_save_file()
    screen = pygame.display.set_mode((init_settings.screen_width, init_settings.screen_height))
    screen.fill(init_settings.background_colour)

    pygame.display.set_caption("Test")

    while True:
        keys.check_events()


if __name__ == "__main__":
    main()