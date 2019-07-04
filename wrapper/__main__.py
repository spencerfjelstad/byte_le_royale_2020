import sys

from game.utils.generate_game import generate
from game.main import loop
from game.config import *

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No arguments given. Append "-help" for a list of them.')
        exit()
    
    # Generate game options
    if '-generate' in sys.argv:
        generate()
    
    # Run game options
    elif '-run' in sys.argv:
        loop()
    
    # Visualizer options
    elif '-visualizer' in sys.argv:
        # importing in the middle of a file is not good practice but its done here to quiet pygame for non-visualizer options
        from game.visualizer import start
        
        # Additional args
        full = False
        gamma = GAMMA
        if '-fullscreen' in sys.argv:
           full = True 
        if '-gamma' in sys.argv:
            gamma_in = sys.argv.index('-gamma') + 1
            if len(sys.argv) > gamma_in:
                gamma = float(sys.argv[gamma_in])
            else:
                print('Gamma input not found, using default value')
                
            print(gamma)
        start(gamma, full)
        
    # Help
    elif '-help' in sys.argv:
        print("Here's a list of arguments:")
        print("-generate")
        print("-run")
        print("-visualizer  |  subarguments:[-fullscreen, -gamma]")