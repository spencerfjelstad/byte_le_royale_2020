from game.common.disasters import LastingDisaster
from game.common.enums import *
from game.utils.oop import *


class Fire(LastingDisaster):
    @overrides
    def __init__(self):
        super().__init__()
        self.damage = 50
        self.effort_remaining = 100
        self.status = DisasterStatus.live
        self.type = DisasterType.fire
