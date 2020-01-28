from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.number = 100
        self.SENSOR_DECREE_MAPPINGS = {
            SensorType.fire_alarm: DecreeType.anti_fire_dogs,
            SensorType.rock_on_a_rope: DecreeType.paperweights,
            SensorType.coast_guard: DecreeType.snow_shovels,
            SensorType.seismograph: DecreeType.rubber_boots,
            SensorType.scp_foundation: DecreeType.fishing_hook,
            SensorType.satellite_dish: DecreeType.cheese
        }

        self.lasting_disasters = [DisasterType.fire, DisasterType.blizzard, DisasterType.monster]

    def team_name(self):
        return "Scummy Fungus"

    def city_name(self):
        return "Bingy Spingus"

    def city_type(self):
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):
        self.print('New Turn')
        # Set decree to highest odds
        highest = -1
        highest_sensor = None
        for sensor in city.sensors.values():
            if sensor.sensor_results > highest:
                highest = sensor.sensor_results
                highest_sensor = sensor

        corresponding_decree = self.SENSOR_DECREE_MAPPINGS[highest_sensor.sensor_type]
        actions.set_decree(corresponding_decree)

        current_lasting_disasters = [x for x in disasters if x.type in self.lasting_disasters]

        total_effort_spent = 0
        things_done = list()
        while total_effort_spent < city.population:
            effort_remaining = city.population - total_effort_spent
            self.print(f'Spent: {total_effort_spent} | Remaining: {effort_remaining} | Total: {city.population}')

            effort_spent = 0
            act = None

            # Allocate effort to repairing the city structure
            if city.structure < city.max_structure and ActionType.repair_structure not in things_done:
                self.print('Fixing structure')
                difference = city.max_structure - city.structure
                effort_spent = min(4 * difference, effort_remaining)
                act = ActionType.repair_structure

            # Allocate effort to recovering population
            elif city.population < city.max_structure and ActionType.regain_population not in things_done:
                self.print('Recovering population')
                difference = city.max_structure - city.population
                effort_spent = min(4 * difference, effort_remaining)
                act = ActionType.regain_population

            # Allocate effort to disasters
            elif len(current_lasting_disasters) > 0:
                self.print('Getting rid of disaster')
                disaster = None
                threat_score = -float('INF')
                for d in current_lasting_disasters:
                    ts = d.effort_remaining * (1 / (d.population_damage + d.structure_damage))
                    if ts >= threat_score:
                        disaster = d
                        threat_score = ts

                if disaster is not None:
                    effort_spent = min(disaster.effort_remaining, effort_remaining)
                    act = disaster
                    current_lasting_disasters.remove(disaster)

            # Allocate effort to upgrading the city
            elif city.level != CityLevel.level_three and ActionType.upgrade_city not in things_done:
                self.print('Upgrading city')
                effort_spent = min(city.effort_remaining, effort_remaining)
                act = ActionType.upgrade_city

            # Build wealth building
            elif city.gold > effort_remaining and \
                    city.buildings[BuildingType.wealth_booster].level != BuildingLevel.level_three and \
                    city.buildings[BuildingType.wealth_booster] not in things_done:
                self.print('Building wealth building')
                effort_spent = min(city.buildings[BuildingType.wealth_booster].effort_remaining, effort_remaining)
                act = city.buildings[BuildingType.wealth_booster]

            # Build canoe
            elif city.gold > effort_remaining and \
                    city.buildings[BuildingType.everything_booster].level != BuildingLevel.level_three and \
                    city.buildings[BuildingType.everything_booster] not in things_done:
                self.print('Building structure building')
                effort_spent = min(city.buildings[BuildingType.everything_booster].effort_remaining, effort_remaining)
                act = city.buildings[BuildingType.everything_booster]

            # Build population building
            elif city.gold > effort_remaining and \
                    city.buildings[BuildingType.population_booster].level != BuildingLevel.level_three and \
                    city.buildings[BuildingType.population_booster] not in things_done:
                self.print('Building population building')
                effort_spent = min(city.buildings[BuildingType.population_booster].effort_remaining, effort_remaining)
                act = city.buildings[BuildingType.population_booster]

            # Build population building
            elif city.gold > effort_remaining and \
                    city.buildings[BuildingType.structure_booster].level != BuildingLevel.level_three and \
                    city.buildings[BuildingType.structure_booster] not in things_done:
                self.print('Building structure building')
                effort_spent = min(city.buildings[BuildingType.structure_booster].effort_remaining, effort_remaining)
                act = city.buildings[BuildingType.structure_booster]

            # Build instant decree building
            elif city.gold > effort_remaining and \
                    city.buildings[BuildingType.instant_decree_booster].level != BuildingLevel.level_three and \
                    city.buildings[BuildingType.instant_decree_booster] not in things_done:
                self.print('Building structure building')
                effort_spent = min(city.buildings[BuildingType.instant_decree_booster].effort_remaining,
                                   effort_remaining)
                act = city.buildings[BuildingType.instant_decree_booster]

            # Get gold otherwise
            else:
                self.print('Getting gold')
                effort_spent = effort_remaining
                act = ActionType.accumulate_wealth

            actions.add_effort(act, effort_spent)
            things_done.append(act)
            total_effort_spent += effort_spent
