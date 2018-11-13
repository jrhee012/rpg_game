import os
import sys


class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (255, 255, 255)

    def check_save_file(self):
        ROOT_DIR = os.path.dirname(sys.modules['__main__'])
        print(ROOT_DIR)
        dir = os.path.join(ROOT_DIR, 'configuration', 'test', 'a', 'b')
        print(dir)

