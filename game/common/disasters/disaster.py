from abc import ABC, abstractmethod
from game.common.enums import *


class Disaster(ABC):
    @abstractmethod
    def __init__(self):
        self.status = DisasterStatus.dead
        self.type = None
        self.population_damage = None
        self.structure_damage = None

    def destroy(self):
        self.status = DisasterStatus.dead
