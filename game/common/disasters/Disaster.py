from abc import ABC
from game.common.enums import *


class Disaster(ABC):
    def __init__(self):
        self.status = DisasterStatus.dead
        self.type = None
        self.damage = 0

    def destroy(self):
        self.status = DisasterStatus.dead
