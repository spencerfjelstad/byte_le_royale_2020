from game.client.user_client import UserClient
from game.common.enums import *


#class Clint(UserClient):
class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        #super().__init__()
        pass

    def team_name(self):
        return "Oops"

    def city_nme(self):
        return "Woops"

    def city_type(self):
        return CityType.sturdy

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        #x = 1 / 0

        #while True:
        #    pass

        actions.vermont('hi')
