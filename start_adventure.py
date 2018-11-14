import pygame
from GameFunction import settings, keys, screen
from Logger import log

# __APP__: list = []
__MAIN_LOGGER__ = "MAIN"
app = []


class App:
    def __init__(self):
        self.settings = None
        self.screen = None
        self.name = "MAIN APP"
        self.state = None

        # app.append(self)
        # print('asdasd:::', app)
        self.main()

    def main(self) -> None:
        pygame.init()

        key_listener = keys.KeyListener(name="MAIN_KEY_LISTENER")

        init_settings = settings.Settings()
        init_settings.initialize(self, key_listener)
        self.settings = init_settings

        game_screen = screen.Screen(init_settings)
        self.screen = game_screen

        # push_to_app(self)
        # app = self

        while True:
            # keys.check_events()
            key_listener.check_events(self)

#
# def push_to_app(main:App) -> None:
#     app.append(main)
#     print('push app', app)
#
#
# def get_app():
#     print(app)
#     return app[0]


if __name__ == "__main__":
    log.Logger(__MAIN_LOGGER__)
    app = App()