import sys

from game.engine import loop
from game.utils.generate_game import generate
from scrimmage.client import Client
import game.config
import argparse


if __name__ == '__main__':
    #Setup Argument Parser and Version Number
    par = argparse.ArgumentParser()
    #Add Arguments for the Parser to look for
    par.add_argument('-generate', '-g', action='store_true',default=False,
    dest='gen_bool', help='Generates a new game')

    par.add_argument('-run', '-r', action='store_true', default=False,
    dest='run_bool', help='Runs your AI through the game')
    
    par.add_argument('-debug', '-d', action='store',dest='debug'
    , type=int,help='Allows for debugging, subargument of -run')
    
    par.add_argument('-quiet','-q',action='store_true',default=False,
    dest='q_bool',help='Runs AI quietly, subargument of -run')
    
    par.add_argument('-visualizer', '-v', action='store_true',default=False,
    dest='vis_bool', help='Runs the visualizer')
    
    par.add_argument('-fullscreen','-f',action='store_true',default=False,
    dest='full_bool',help='Runs visualizer in full screen, subarg of -v')
    
    par.add_argument('-gamma','-ga', action='store', dest='gamma',
    help='Allows setting of gamma value, subarg of -v')

    par.add_argument('-skip','-sk',action='store_true',default=False,
    dest='skip_bool',help='Skips end screen, subarg of -v')

    par.add_argument('-scrimmage','-s',action='store_true',default=False,
    dest='scrim_bool',help='Boots the scrimmage server')

    args = par.parse_args()

    # Generate game options
    if  args.gen_bool:
        generate()
    
    # Run game options
    elif args.run_bool:
        # Additional args
        quiet = False
        if args.debug != None:
            if len(sys.argv) > args.debug:
                game.config.Debug.level = int(sys.argv[args.debug])
            else:
                print('Debug input not found, using default value')
        if args.q_bool:
            quiet = True

        loop(quiet)
    
    # Visualizer options
    elif args.vis_bool:
        # importing in the middle of a file is not good practice but it's done here to quiet pygame for non-visualizer options
        from game.visualizer import start
        
        # Additional args
        full = False
        gamma = game.config.GAMMA
        endgame = True
        if args.full_bool:
            full = True
        if args.gamma != None:
            if len(sys.argv) > args.gamma:
                gamma = float(sys.argv[args.gamma])
            else:
                print('Gamma input not found, using default value')
        if args.skip_bool:
            endgame = False


        start(gamma, full, endgame)
        
    # Boot up the scrimmage server client
    elif args.scrim_bool:
        cl = Client()
