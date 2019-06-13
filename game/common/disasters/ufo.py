from game.common.disasters.disaster import Disaster
from game.common.enums import *
from game.common.stats import GameStats
from game.utils.oop import *


class Ufo(Disaster):
    def __init__(self):
        super().__init__()
        self.status = DisasterStatus.live
        self.type = DisasterType.ufo
        self.population_damage = GameStats.disaster_population_damages[self.type]
        self.structure_damage = GameStats.disaster_structure_damages[self.type]