from game.common.disasters.disaster import Disaster
from game.common.enums import *


class LastingDisaster(Disaster):
    def __init__(self, level=DisasterLevel.level_zero):
        super().__init__(level)
        self.newly_spawned = True
        self.initial_effort = None
        self.effort_remaining = None

    def reduce(self, effort):
        if effort < 0:
            raise ValueError("effort should be positive!")

        self.effort_remaining -= effort

        if self.effort_remaining <= 0:
            self.destroy()

    def to_json(self):
        data = Disaster.to_json(self)

        data["newly_spawned"] = self.newly_spawned
        data["initial_effort"] = self.initial_effort
        data["effort_remaining"] = self.effort_remaining

        return data

    def from_json(self, data):
        Disaster.from_json(self, data)

        self.newly_spawned = data["newly_spawned"]
        self.initial_effort = data["initial_effort"]
        self.effort_remaining = data["effort_remaining"]
