import pygame
import sys
import logging

logger = logging.getLogger("MAIN")
active_key_listeners: list = []


class KeyListener:

    def __init__(self, name: str = ""):
        self.name = name
        logger.info("%s started!" % self.name)
        active_key_listeners.append(self)

    # def __getitem__(self, item):


    @staticmethod
    def check_keydown_events(event):
        if event.key == pygame.K_RIGHT:
            print('right!!!')
        elif event.key == pygame.K_LEFT:
            print('left!!!')
        elif event.key == pygame.K_SPACE:
            print('space!!!')
        elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            sys.exit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                print('key up!!!')
                # check_keyup_events()

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
