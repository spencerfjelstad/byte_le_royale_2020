import sys

from game.utils.generate_game import generate
from game.engine import loop
import game.config

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No arguments given. Append "-help" for a list of them.')
        exit()
    
    # Generate game options
    if '-generate' in sys.argv:
        generate()
    
    # Run game options
    elif '-run' in sys.argv:
        # Additional args
        if '-debug' in sys.argv:
            debug_in = sys.argv.index('-debug') + 1
            if len(sys.argv) > debug_in:
                game.config.Debug.level = int(sys.argv[debug_in])
            else:
                print('Debug input not found, using default value')

        loop()
    
    # Visualizer options
    elif '-visualizer' in sys.argv:
        # importing in the middle of a file is not good practice but it's done here to quiet pygame for non-visualizer options
        from game.visualizer import start
        
        # Additional args
        full = False
        gamma = game.config.GAMMA
        endgame = True
        if '-fullscreen' in sys.argv:
            full = True
        if '-gamma' in sys.argv:
            gamma_in = sys.argv.index('-gamma') + 1
            if len(sys.argv) > gamma_in:
                gamma = float(sys.argv[gamma_in])
            else:
                print('Gamma input not found, using default value')
        if '-skip' in sys.argv:
            endgame = False


        start(gamma, full, endgame)
        
    # Help
    elif '-help' in sys.argv:
        print("Here's a list of arguments:")
        print("-generate")
        print("-run         |  subarguments:[-debug x]")
        print("-visualizer  |  subarguments:[-fullscreen, -gamma x]")
