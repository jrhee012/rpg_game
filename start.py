import pygame
from GameFunction import settings, keys, character


def main():

    pygame.init()

    init_settings = settings.Settings()

    init_settings.initialize()

    screen = pygame.display.set_mode((init_settings.screen_width, init_settings.screen_height))
    screen.fill(init_settings.background_colour)

    pygame.display.set_caption('Test')

    new = character.Character()
    print(new.get_info())

    while True:
        keys.check_events()


if __name__ == '__main__':
    main()