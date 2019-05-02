from game.common.enums import *

# Game Generation
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

