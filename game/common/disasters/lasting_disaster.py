from abc import abstractmethod
from game.common.disasters.disaster import Disaster
from game.utils.oop import *


class LastingDisaster(Disaster):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.initial_effort = None
        self.effort_remaining = None

    def reduce(self, effort):
        if effort < 0:
            raise ValueError("effort should be positive!")

        self.effort_remaining -= effort

        if self.effort_remaining <= 0:
            self.destroy()
