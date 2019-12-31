from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return "Hodd Toward"

    def city_name(self):
        return "It just works"

    def city_type(self):
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):
        actions.set_decree(DecreeType.anti_fire_dogs)
        if len(disasters) > 0 and disasters[0].type in [DisasterType.fire, DisasterType.blizzard, DisasterType.monster]:
            actions.add_effort(disasters[0], disasters[0].effort_remaining)
        actions.add_effort(ActionType.regain_population, city.population / 3)
        actions.add_effort(ActionType.repair_structure, city.population / 3)
        actions.add_effort(ActionType.upgrade_city, city.population / 3)
