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

    log_parser = GameLogParser("logs/")

    # initialize pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.font.init()

    global global_surf
    if fullscreen:
        global_surf = pygame.display.set_mode(DISPLAY_SIZE)#, pygame.FULLSCREEN)
    else:
        global_surf = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption('Byte-le Royale: Shitty City')

    pygame.display.set_gamma(gamma)

    # prep for game loop
    first_loop = True
    turn_wait_counter = 1

    # the big boy
    while True:

        if not pause:

            if first_loop:
                first_loop = False

            draw_screen()

            handle_events()

            pygame.display.update()
            fpsClock.tick(_FPS)
        else:
            handle_events()


def draw_screen():
    global global_surf
    global log_parser
    # clear screen
    global_surf.fill(pygame.Color(0, 0, 0))

    # This is all trash for testing
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30, True)

    turn_info = log_parser.get_turn()
    if turn_info is None:
        pygame.quit()
        sys.exit(0)
    turn = font.render(f'Turn {log_parser.tick}', True, (150, 140, 130))
    global_surf.blit(turn, (30, 500))
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
