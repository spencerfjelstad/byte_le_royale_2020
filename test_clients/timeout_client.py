from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.i = 0

    def team_name(self):
        return "Timeout"

    def city_name(self):
        return "Timeout Town"

    def city_type(self):
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        while self.i < 1_000_000_000_000:
            self.i += 1
