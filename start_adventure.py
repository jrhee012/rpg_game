import pygame
from GameFunction import settings, keys
from Logger import log


class App:

    def __init__(self):
        self.main()

    @staticmethod
    def main() -> None:
        pygame.init()

        init_settings = settings.Settings()

        init_settings.initialize()

        screen = pygame.display.set_mode((init_settings.screen_width, init_settings.screen_height))
        screen.fill(init_settings.background_colour)

        pygame.display.set_caption("Test")

        key_listener = keys.KeyListener(name="MAIN_KEY_LISTENER")

        # keys.find_key_listener("test")

        while True:
            # keys.check_events()
            key_listener.check_events()


if __name__ == "__main__":
    log.Logger("MAIN")
    App()