# CLIENT THAT FOCUSES ON INCREASING POPULATION LEVEL (through tourism) TO KEEP CITY GOING
from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return "Tourism-R-Us"

    def city_name(self):
        return "Hawaii"

    def city_type(self):
        return CityType.none

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):
        actions.add_effort(ActionType.repair_structure, city.population/2)
        actions.add_effort(ActionType.regain_population, city.population/2)
        actions.set_decree(DecreeType.paperweights)
