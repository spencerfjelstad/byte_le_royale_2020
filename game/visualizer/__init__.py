import sys
import math
import random
import time
import zipfile

import pygame
from pygame.locals import *

from game.visualizer.game_log_parser import GameLogParser
from game.config import *

pause = False
log_parser = None
global_surf = None
fpsClock = None
turn = 0 # current turn of the visualizer

debug = False

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
    global_surf.fill(pygame.Color(0, 0, 0))

    # This is all trash for testing
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30, True)

    turn_info = log_parser.get_turn(current_turn)
    if turn_info is None:
        pygame.quit()
        sys.exit(0)
    turn_indicator = font.render(f'Turn {turn}', True, (150, 140, 130))
    global_surf.blit(turn_indicator, (30, 500))
    n = 0
    for key, item in turn_info['rates'].items():
        n += 1
        text = f'{key}: {item}'
        render_text = font.render(text, True, (0, 150, 150))
        global_surf.blit(render_text, (30, 30*n))


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