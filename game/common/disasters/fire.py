from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.stats import GameStats


class Fire(LastingDisaster):
    def __init__(self, level=DisasterLevel.level_zero):
        super().__init__(level)
        self.initial_effort = GameStats.disaster_initial_efforts[DisasterType.fire]
        self.effort_remaining = self.initial_effort
        self.status = DisasterStatus.live
        self.type = DisasterType.fire
        self.population_damage = GameStats.disaster_population_damages[self.type][self.level]
        self.structure_damage = GameStats.disaster_structure_damages[self.type][self.level]
