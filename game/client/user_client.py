from game.common.enums import DebugLevel
from game.config import Debug


class UserClient:
    def __init__(self):
        self.my_decree = None
        self.debug_level = DebugLevel.client
        self.debug = True

    def print(self, *args):
        if self.debug and Debug.level >= self.debug_level:
            print(f'{self.__class__.__name__}: ', end='')
            print(*args)

    def team_name(self):
        return "No_Team_Name_Available"

    def city_name(self):
        return "No_City_Name_Available"

    def set_decree(self, my_decree):
        raise NotImplementedError("TODO: implement this function in UserClient")

    def take_turn(self, actions, city, disasters):
        raise NotImplementedError("Implement this in subclass")

    # TODO: Discuss full list of actions
