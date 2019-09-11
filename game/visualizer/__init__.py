import sys
import math
import random
import time
import zipfile

import pygame
from pygame.locals import *

from game.visualizer.game_log_parser import GameLogParser
from game.utils.helpers import *
from game.common.enums import *
from game.visualizer.graphs import *
from game.config import *
from game.common.stats import *
from game.visualizer.city_sprites import *
from game.visualizer.location_sprites import *

pause = False
log_parser = None
global_surf = None
fpsClock = None
turn = 0  # current turn of the visualizer

debug = False

# Sprite Groups
city_group = pygame.sprite.Group()
location_group = pygame.sprite.Group()

_VIS_INTERMEDIATE_FRAMES = VIS_INTERMEDIATE_FRAMES
_FPS = FPS


def log(msg):
    if debug:
        print(str(msg))


def start(gamma, fullscreen=False):
    global pause
    global fpsClock
    global log_parser
    global turn

    log_parser = GameLogParser("logs/")

    # initialize pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.font.init()

    global global_surf
    if fullscreen:
        global_surf = pygame.display.set_mode(DISPLAY_SIZE, pygame.FULLSCREEN)
    else:
        global_surf = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption('Byte-le Royale: Disaster Dispatcher')

    pygame.display.set_gamma(gamma)

    # Sprite changing logic
    city_x = 484
    city_y = 200
    city_struct = GameStats.city_structure

    # Checks city_structure and draws sprite accordingly
    if city_struct <= GameStats.city_structure / 3:
        city_sprite = CitySpriteLevel0(city_x, city_y, CityLevel.level_zero)
        city_group.add(city_sprite)
    elif city_struct <= GameStats.city_structure / 2:
        city_sprite = CitySpriteLevel0(city_x, city_y, CityLevel.level_one)
        city_group.add(city_sprite)
    elif city_struct <= GameStats.city_structure:
        city_sprite = CitySpriteLevel0(city_x, city_y, CityLevel.level_two)
        city_group.add(city_sprite)

    location_sprite = LocationDefault(0,0, CityLocation.default)
    location_group.add(location_sprite)

    # prep for game loop
    turn_wait_counter = 1

    # the big boy
    while True:

        handle_events()

        if not pause:
            # increment forward and display page
            turn += 1
            show()


# Update the visualizer to display the current turn data
def show():
    global turn
    draw_screen(turn)
    pygame.display.update()
    fpsClock.tick(_FPS)


def draw_screen(current_turn):
    global global_surf
    global log_parser
    global turn

    # clear screen
    global_surf.fill(pygame.Color(128, 212, 255))

    # Draw groups
    location_group.draw(global_surf)
    city_group.draw(global_surf)

    # # This is all trash for testing
    # font = pygame.font.SysFont(pygame.font.get_default_font(), 30, True)
    #
    # if turn_info is None:
    #     pygame.quit()
    #     sys.exit(0)
    # turn_indicator = font.render(f'Turn {turn}', True, (150, 140, 130))
    # global_surf.blit(turn_indicator, (30, 500))
    # n = 0
    # for key, item in turn_info['rates'].items():
    #     n += 1
    #     text = f'{key}: {item}'
    #     render_text = font.render(text, True, (0, 150, 150))
    #     global_surf.blit(render_text, (30, 30*n))

    # This is all trash for testing
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30, True)

    turn_info = log_parser.get_turn(current_turn)
    if turn_info is None:
        endgame()
    turn_indicator = font.render(f'Turn {turn}', True, (150, 140, 130))
    health_bar(turn_info, global_surf)
    global_surf.blit(turn_indicator, (30, 500))
    n = 0
    for key, item in turn_info['rates'].items():
        n += 1
        text = f'{key}: {item}'
        render_text = font.render(text, True, (0, 150, 150))
        global_surf.blit(render_text, (30, 30*n))


# Display endgame screen
def endgame():
    global_surf.fill(pygame.Color(0, 255, 255))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = font.render('Some Text', False, (0, 0, 0))
    global_surf.blit(textsurface,(0,0))
    # Draws graph of round's data
    lineGraph(global_surf)

    pygame.display.update()

    # Stays running till exit button pressed
    while True:
        handle_events()


def handle_events():
    for event in pygame.event.get():
        # Application exited by user
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard events
        elif event.type == KEYUP:
            global turn

            # Pause toggle
            if event.key == K_p:
                global pause
                pause = not pause

            # Toggle fullscreen (may not work on windows)
            if event.key == K_f:
                pygame.display.toggle_fullscreen()

            # Exit
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Back up a turn
            if event.key == K_LEFT:
                turn -= 1
                show()

            # Forward a turn
            if event.key == K_RIGHT:
                turn += 1
                show()

            # start
            if event.key == K_DOWN:
                turn = 1
                show()

            # end
            if event.key == K_UP:
                turn = MAX_TURNS
                show()

            # yeet
            if event.key == K_y:
                turn = random.randint(1, MAX_TURNS)
                show()