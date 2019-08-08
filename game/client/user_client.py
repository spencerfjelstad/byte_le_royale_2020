from abc import ABC, abstractmethod

from game.common.enums import DebugLevel
from game.config import Debug


class UserClient(ABC):
    def __init__(self):
        self.my_decree = None
        self.debug_level = DebugLevel.client
        self.debug = True

    def print(self, *args):
        if self.debug and Debug.level >= self.debug_level:
            print(f'{self.__class__.__name__}: ', end='')
            print(*args)

    @staticmethod
    def team_name():
        return "No_Team_Name_Available"

    def set_decree(self, my_decree):
        raise NotImplementedError("TODO: implement this function in UserClient")

    @abstractmethod
    def take_turn(self, actions, city, disasters):
        raise NotImplementedError("Implement this in subclass")

    # TODO: Discuss full list of actions
