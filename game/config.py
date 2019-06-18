from game.common.enums import *
import platform

# Game Generation
# WARNING: Game will not function properly if MAX_TURNS is set beyond 9999.
MAX_TURNS = 2000

INDIVIDUAL_WEIGHTS = {
    DisasterType.fire : 0.01,
    DisasterType.tornado : 0.01,
    DisasterType.hurricane : 0.005,
    DisasterType.earthquake : 0.005,
    DisasterType.monster : 0.001,
    DisasterType.ufo : 0.001,
}

DISASTER_CHANCE_GROWTH_RATE = 1 / (MAX_TURNS / 4)
STARTING_FREE_TURNS = 10
ACTIVATION_DEPRECIATION_RATE = 0.95

# Runtime settings / Restrictions
MAX_OPERATIONS_PER_TURN = 25000
MAX_ALLOCATIONS_ALLOWED_PER_TURN = 30

# Visualizer business
DISPLAY_SIZE = (1280, 720)
GAMMA = 0
if platform.system() == 'Linux':
    VIS_INTERMEDIATE_FRAMES = 10
    FPS = 60
    LOW_FPS = 30
else:
    VIS_INTERMEDIATE_FRAMES = 4
    FPS = 120
    LOW_FPS = 60
