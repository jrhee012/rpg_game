# import sys
import pygame
import GameFunction.keys


def main():
    pygame.init()

    screen_height = 1200
    screen_width = 1000
    background_colour = (255, 255, 255)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test")
    screen.fill(background_colour)

    while True:
        GameFunction.keys.check_events()


if __name__ == "__main__":
    main()