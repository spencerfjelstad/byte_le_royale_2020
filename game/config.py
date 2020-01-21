from game.common.enums import *
import os
import platform

# Runtime settings / Restrictions --------------------------------------------------------------------------------------
# The engine requires these to operate
MAX_TURNS = 2000                                    # max number of ticks the server will run regardless of game state
TQDM_BAR_FORMAT = "Game running at {rate_fmt} "     # how TQDM displays the bar
TQDM_UNITS = " turns"                               # units TQDM takes in the bar

MAX_OPERATIONS_PER_TURN = 450000                    # max number of basic operations clients have for their turns

MIN_CLIENTS_START = None                            # minimum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_START = None                            # maximum number of clients required to start running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_START = 1                     # required number of clients to start running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used
CLIENT_KEYWORD = "client"                           # string required to be in the name of every client file, not found otherwise
CLIENT_DIRECTORY = "./"                             # location where client code will be found


MIN_CLIENTS_CONTINUE = None                         # minimum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
MAX_CLIENTS_CONTINUE = None                         # maximum number of clients required to continue running the game; should be None when SET_NUMBER_OF_CLIENTS is used
SET_NUMBER_OF_CLIENTS_CONTINUE = 1                  # required number of clients to continue running the game; should be None when MIN_CLIENTS or MAX_CLIENTS are used

ALLOW_ONLY_MODE = False                             # If True, only ALLOWED_MODULES can be imported by the client
ALLOWED_MODULES = ["game.client.user_client",       # modules that clients are specifically allowed to access
                   "game.common.enums"]
RESTRICTED_MODULES = ["game",                       # modules that clients will be prevented from accessing
                      "importlib",
                      "os",
                      "sys"]

# Game Rule settings ---------------------------------------------------------------------------------------------------
MAX_ALLOCATIONS_ALLOWED_PER_TURN = 30               # max number of unique effort allocations clients are allowed


# Keeps track of the current debug level of the game (not a variable because it won't save when changed that way)
class Debug:
    level = DebugLevel.none


# Game Generation ------------------------------------------------------------------------------------------------------
APPROXIMATE_DISASTER_COUNT = 250    # approximate number of disasters to be spawned over the course of time
DISASTER_BIAS = 0.35                # percent of how many disasters will be located in the first half of the game, float less than 1 and greater than 0
BIASING_DEPTH = 16                  # how deep the recursive biasing strategy will go, higher is more accurate
BIAS_MARGIN_OF_ERROR = 0.8          # range around DISASTER_BIAS where the biasing will be accepted, float less than 1 and greater than 0

# Breakdown percentages of approximately how many disasters of each type will spawn (must total to 1)
DISASTER_WEIGHTS = {
    DisasterType.fire: 0.30,
    DisasterType.tornado: 0.30,
    DisasterType.blizzard: 0.15,
    DisasterType.earthquake: 0.15,
    DisasterType.monster: 0.05,
    DisasterType.ufo: 0.05,
}

STARTING_FREE_TURNS = 10            # how many turns at the beginning will be guaranteed free of disasters

# Visualizer business --------------------------------------------------------------------------------------------------
DISPLAY_SIZE = (1280, 720)          # resolution of the game window
GAMMA = 1                           # monitor brightness
# Used to help the game run better on Linux
if platform.system() == 'Linux':
    VIS_INTERMEDIATE_FRAMES = 10
    FPS = 60
    LOW_FPS = 30
else:
    VIS_INTERMEDIATE_FRAMES = 4
    FPS = 120
    LOW_FPS = 60

# Results file ---------------------------------------------------------------------------------------------------------
RESULTS_FILE_NAME = "results.json"                              # Name and extension of results file
RESULTS_DIR = os.path.join(os.getcwd(), "logs")                 # Location of the results file
RESULTS_FILE = os.path.join(RESULTS_DIR, RESULTS_FILE_NAME)     # Results directory combined with file name
