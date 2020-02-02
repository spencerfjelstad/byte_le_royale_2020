from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.previous_disaster = None

        self.lasting_disasters = [DisasterType.fire, DisasterType.blizzard, DisasterType.monster]

        self.disaster_to_decree = {
            DisasterType.fire: DecreeType.anti_fire_dogs,
            DisasterType.tornado: DecreeType.paperweights,
            DisasterType.blizzard: DecreeType.snow_shovels,
            DisasterType.earthquake: DecreeType.rubber_boots,
            DisasterType.monster: DecreeType.fishing_hook,
            DisasterType.ufo: DecreeType.cheese,
        }

    def team_name(self):
        return 'Team Name'

    def city_name(self):
        return 'City Name'

    def city_type(self):
        return CityType.popular

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        # If there is a lasting disaster, take care of it
        for disaster in disasters:
            if disaster.type in self.lasting_disasters:
                # Allocate 1/4 of our current population to putting it out
                actions.add_effort(disaster, city.population / 4)
                self.print(f'Uh oh, better fix the disaster: {disaster.type}!')

            self.previous_disaster = disaster

        # Fix up our city
        if city.structure != city.max_structure:
            # No object represents structure, so we use the ActionType enum here
            actions.add_effort(ActionType.repair_structure, 40)
        if city.population != city.structure:
            # Same thing with regaining population
            actions.add_effort(ActionType.regain_population, 40)

        # Upgrade my favorite sensor <3
        if city.sensors[SensorType.tornado].level != SensorLevel.level_three:
            # Retrieve tornado sensor and put effort towards upgrading it
            actions.add_effort(city.sensors[SensorType.tornado], 120)

        # Set the decree
        decree = DecreeType.none
        if self.previous_disaster is not None:
            decree = self.disaster_to_decree[self.previous_disaster.type]
        actions.set_decree(decree)
