import pygame
import sys
import logging
from enum import Enum

logger = logging.getLogger("MAIN")
active_key_listeners: list = []


class KeyInput(Enum):
    UP: str = "UP"
    DOWN: str = "DOWN"
    LEFT: str = "LEFT"
    RIGHT: str = "RIGHT"
    Q: str = "Q"
    RETURN: str = "RETURN"
    SPACE: str = "SPACE"
    ESC: str = "ESCAPE"


class KeyListener:
    def __init__(self, name: str = ""):
        self.name = name
        self.app = None

        logger.info("%s started!" % self.name)
        active_key_listeners.append(self)

    @staticmethod
    def process_keydown_events(event, app):
        if event.key == pygame.K_RIGHT:
            print('right!!!')
        elif event.key == pygame.K_LEFT:
            print('left!!!')
        elif event.key == pygame.K_UP:
            print('up!!!')
        elif event.key == pygame.K_DOWN:
            print('down!!!')
        elif event.key == pygame.K_SPACE:
            print('space!!!')
        elif event.key == pygame.K_RETURN:
            print('enter!!!')
            # app = start_adventure.get_app("test")
            # print('apppp: ', app.state)
            app.state.update()
        elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            sys.exit()

    # def keydown_action(self, key: KeyInput, state: State):
    #     if state.name == StateValue.START_SCREEN:

    def check_events(self, app):
        self.app = app

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.process_keydown_events(event, app)

            # elif event.type == pygame.KEYUP:
            #     print('key up!!!')

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print('mouse!!!', mouse_x, mouse_y)


def search_key_listener(name: str = "MAIN_KEY_LISTENER") -> KeyListener:
    result: KeyListener = None
    for listener in active_key_listeners:
        print('name....', listener.name)
        if listener.name == name:
            result = listener
            break

    if result is None:
        raise FileNotFoundError

    return result


def find_key_listener(name: str = "MAIN_KEY_LISTENER") -> KeyListener:
    result: KeyListener = None

    try:
        result = search_key_listener(name)
    except FileNotFoundError:
        logger.debug("Key Listener With Name - %s Not Found!" % name)

    return result
