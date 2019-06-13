from abc import abstractmethod
from game.common.disasters.disaster import Disaster
from game.utils.oop import *
from game.common.enums import *


class LastingDisaster(Disaster):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.initial_effort = None
        self.effort_remaining = None
        self.object_type = ObjectType.lasting_disaster

    def reduce(self, effort):
        if effort < 0:
            raise ValueError("effort should be positive!")

        self.effort_remaining -= effort

        if self.effort_remaining <= 0:
            self.destroy()

    def to_json(self):
        data = Disaster.to_json()

        data["initial_effort"] = self.initial_effort
        data["effort_remaining"] = self.effort_remaining

        return data

    def from_json(self, data):
        Disaster.from_json(data)

        self.initial_effort = data["inital_effort"]
        self.effort_remaining = data["effort_remaining"]
