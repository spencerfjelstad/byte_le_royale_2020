from game.common.disasters import Disaster
from game.utils.oop import *


class LastingDisaster(Disaster):
    @overrides
    def __init__(self):
        super().__init__()
        self.effort_remaining = 0

    def reduce(self, effort):
        if effort < 0:
            raise ValueError("effort should be positive!")

        self.effort_remaining -= effort

        if self.effort_remaining <= 0:
            self.destroy()
