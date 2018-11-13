import pygame
import sys


def check_keydown_events(event):
    if event.key == pygame.K_RIGHT:
        print('right!!!')
    elif event.key == pygame.K_LEFT:
        print('left!!!')
    elif event.key == pygame.K_SPACE:
        print('space!!!')
    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        sys.exit()

# def check_keyup_events(event, ship):
    # if event.key == pygame.K_RIGHT:
    #     ship.moving_right = False
    # elif event.key == pygame.K_LEFT:
    #     ship.moving_left = False


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

        elif event.type == pygame.KEYUP:
            print('key up!!!')
            # check_keyup_events()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print('mouse!!!', mouse_x, mouse_y)
