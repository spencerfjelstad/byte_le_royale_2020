from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.stats import GameStats


class Hurricane(LastingDisaster):
    def __init__(self):
        super().__init__()
        self.initial_effort = GameStats.disaster_initial_efforts[DisasterType.hurricane]
        self.effort_remaining = self.initial_effort
        self.status = DisasterStatus.live
        self.type = DisasterType.hurricane
        self.population_damage = GameStats.disaster_population_damages[self.type]
        self.structure_damage = GameStats.disaster_structure_damages[self.type]
