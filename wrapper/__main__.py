import sys

from game.engine import loop
from game.utils.generate_game import generate
from scrimmage.client import Client
import version
import updater
import game.config
import argparse

if __name__ == '__main__':
    #Setup Primary Parser
    par = argparse.ArgumentParser()

    # Create Subparsers
    spar = par.add_subparsers(title="Commands", dest="command")

    # Generate Subparser
    gen_subpar = spar.add_parser('generate', aliases=['g'], help='Generates a new random game map')

    # Scrimmage Subparser
    scrim_subpar = spar.add_parser('scrimmage', aliases=['s'], help='Boot client for scrimmage server')
    
    # Run Subparser and optionals
    run_subpar = spar.add_parser('run', aliases=['r'], help='Runs your bot against the last generated map! "r -h" shows more options')

    run_subpar.add_argument('-debug', '-d', action='store', type=int, nargs='?', const=-1, 
    default=None, dest='debug', help='Allows for debugging when running your code')
    
    run_subpar.add_argument('-quiet', '-q', action='store_true', default=False,
    dest='q_bool', help='Runs your AI... quietly :)')

    # Visualizer Subparser and optionals
    vis_subpar = spar.add_parser('visualizer', aliases=['v'], help='Displays your last run through the visualizer! "v -h" shows more options')

    vis_subpar.add_argument('-fullscreen', '-f', action='store_true', default=False,
    dest='full_bool', help='Runs visualizer in fullscreen')
    
    vis_subpar.add_argument('-gamma', '-g', action='store', type=float, nargs='?', const=-1, 
    default=None, dest='gamma', help='Allows manual setting of the gamma value')

    vis_subpar.add_argument('-skip', '-s', action='store_true', default=False,
    dest='skip_bool', help="Skips the visualizer's end screen")

    vis_subpar.add_argument('-place','-p', action='store', type=int, nargs='?', const=-1,
    default=None, dest='place', help='Obfuscates team names with final place')

    # Versioning Subparser
    ver_subpar = spar.add_parser('version', aliases=['e'], help='Displays your current working version of the game')

    # Updating Subparser
    upd_subpar = spar.add_parser('update', aliases=['u'], help='Updates your game to match the newest version if possible')

    # Parse Command Line
    par_args = par.parse_args()
    
    # Main Action variable
    action = par_args.command

    # Generate game options
    if  action in ['generate', 'g']:
        generate()
    
    # Run game options
    elif action in ['run', 'r']:
        # Additional args
        quiet = False

        if par_args.debug is not None:
            if par_args.debug >= 0:
                game.config.Debug.level = par_args.debug
            else:
                print('Valid debug input not found, using default value')
        
        if par_args.q_bool:
            quiet = True

        loop(quiet)
    
    # Visualizer options
    elif action in ['visualizer', 'v']:
        # importing in the middle of a file is not good practice but it's done here to quiet pygame for non-visualizer options
        from game.visualizer import start
        
        # Additional args
        full = False
        gamma = game.config.GAMMA
        endgame = True
        place = None

        if par_args.full_bool:
            full = True

        if par_args.gamma is not None:
            if 1 >= par_args.gamma >= 0:
                gamma = par_args.gamma
            else:
                print('Valid gamma input not found, using default value')

        if par_args.skip_bool:
            endgame = False

        if par_args.place is not None:
            if 3 >= par_args.place >=1:
                place = par_args.place
            else:
                print('Valid place input not found, using default')

        print("Launching visualizer...")
        start(gamma, full, endgame, place)
        
    # Boot up the scrimmage server client
    elif action in ['scrimmage', 's']:
        cl = Client()

    # Version check
    elif action in ['version', 'e']:
        print(version.v)

    # Attempt to update the game
    elif action in ['update', 'u']:
        updater.update()

    # Print help if no arguments are passed
    if len(sys.argv) == 1:
        print("\nLooks like you didn't tell the launcher what to do!"+
        "\nHere's the basic commands in case you've forgotten.\n")
        par.print_help()