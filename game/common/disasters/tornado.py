from game.common.disasters.disaster import Disaster
from game.common.enums import *
from game.common.stats import GameStats


class Tornado(Disaster):
    def __init__(self, level=DisasterLevel.level_zero):
        super().__init__(level)
        self.status = DisasterStatus.live
        self.type = DisasterType.tornado
        self.population_damage = GameStats.disaster_population_damages[self.type][self.level]
        self.structure_damage = GameStats.disaster_structure_damages[self.type][self.level]
