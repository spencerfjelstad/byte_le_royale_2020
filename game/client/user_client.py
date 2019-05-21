from abc import ABC, abstractmethod


class UserClient(ABC):
    def __init__(self):
        self.my_decree = None

    @staticmethod
    def team_name():
        return "No_Team_Name_Available"

    def set_decree(self, my_decree):
        raise NotImplementedError("TODO: implement this function in UserClient")

    @abstractmethod
    def take_turn(self, actions):
        raise NotImplementedError("Implement this in subclass")

    # TODO: Discuss full list of actions
