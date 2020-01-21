from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.lasting_disasters = [
            DisasterType.fire, 
            DisasterType.blizzard, 
            DisasterType.monster
        ]
        
        self.SENSOR_DECREE_MAPPINGS = {
            SensorType.fire_alarm: DecreeType.anti_fire_dogs,
            SensorType.rock_on_a_rope: DecreeType.paperweights,
            SensorType.coast_guard: DecreeType.snow_shovels,
            SensorType.seismograph: DecreeType.rubber_boots,
            SensorType.scp_foundation: DecreeType.fishing_hook,
            SensorType.satellite_dish: DecreeType.cheese
        }

        self.turn = 0

    def team_name(self):
        return "A terrible mess"

    def city_name(self):
        return "Bunker 8925"

    def city_type(self):
        # return CityType.healthy
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):
        self.turn += 1
        # self.print(f"Turn {self.turn}!")
        remaining_effort = city.population

        # Emergency rebuild!!
        # if city.population < city.structure//3:
        #     population_effort = self.clamp(remaining_effort-20, 0, (city.structure//2)-city.population)
        #     self.print(f"Allocated {population_effort} effort to population for emergency rebuild")
        #     remaining_effort -= population_effort

        # if city.structure < city.max_structure//3:
        #     structure_effort = self.clamp(remaining_effort-20, 0, (city.max_structure//2)-city.structure)
        #     self.print(f"Allocated {structure_effort} effort to structure for emergency rebuild")
        #     remaining_effort -= structure_effort

        # if city.population < city.structure//3:
        #     population_effort = self.clamp(remaining_effort-20, 0, (city.structure//2)-city.population)
        #     self.print(f"Allocated {population_effort} effort to population for emergency rebuild")
        #     remaining_effort -= population_effort


        # Put effort towards lasting disasters first
        # disasters_effort = sum(disaster.effort_remaining for disaster in disasters if disaster.type in self.lasting_disasters)
        # disasters_damage = sum(disaster.population_damage + disaster.structure_damage for disaster in disasters if disaster.type in  self.lasting_disasters)
        # self.print(f"Effort: {disasters_effort} and damage: {disasters_damage}")
        remaining_lasting_disasters = self.get_num_lasting(disasters)

        while remaining_effort > 20 and remaining_lasting_disasters > 0:
            self.print("Taking care of disasters!")
            most_damage = -1
            most_damaging = None
            effort_remaining = 99999999999
            for disaster in disasters:
                if disaster.type in self.lasting_disasters:
                    if disaster.population_damage + disaster.structure_damage > most_damage:
                        most_damage = disaster.population_damage + disaster.structure_damage
                        most_damaging = disaster
                        effort_remaining = disaster.effort_remaining
                    elif disaster.population_damage + disaster.structure_damage == most_damage and disaster.effort_remaining < effort_remaining:  # Break ties with lowest effort remaining
                        most_damaging = disaster
                        effort_remaining = disaster.effort_remaining
            self.print(f"Attempting to allocate effort to {most_damaging}")
            effort_added = self.clamp(remaining_effort-20, 0, disaster.effort_remaining)
            actions.add_effort(most_damaging, effort_added)
            remaining_effort -= effort_added
            disasters.remove(most_damaging)
            remaining_lasting_disasters -= 1

        # Population/structure as needed
        if city.population < city.structure:
            population_effort = self.clamp(remaining_effort, 0, city.structure-city.population)
            actions.add_effort(ActionType.regain_population, population_effort)
            remaining_effort -= population_effort
            self.print(f"Added {population_effort} to population!")

        if city.structure < city.max_structure:
            structure_effort = self.clamp(remaining_effort, 0, city.max_structure-city.structure)
            actions.add_effort(ActionType.repair_structure, structure_effort)
            remaining_effort -= structure_effort
            self.print(f"Added {structure_effort} to population!")

        # Upgrade buildings, sensors, and gain gold
        if city.level != CityLevel.level_three:
            actions.add_effort(city, remaining_effort)
        elif city.buildings[BuildingType.everything_booster].level != BuildingLevel.level_three:
            effort_allocated = self.clamp(remaining_effort, 0, city.gold)
            actions.add_effort(city.buildings[BuildingType.everything_booster], effort_allocated)
            remaining_effort -= effort_allocated
        else:
            # Oh jeez now what?!?!?!
            pass
        # Check gold before upgrading buildings!
        
        # Set decree based on highest sensor reading
        highest = -1
        highest_sensor = None
        for sensor in city.sensors.values():
            if sensor.sensor_results > highest:
                highest = sensor.sensor_results
                highest_sensor = sensor
        corresponding_decree = self.SENSOR_DECREE_MAPPINGS[highest_sensor.sensor_type]
        actions.set_decree(corresponding_decree)
        self.print(f"Set decree {corresponding_decree}")

    def clamp(self, value, min_value=0, max_value=100):
        return min(max_value, max(value, min_value))

    def get_num_lasting(self, disasters):
        total = 0
        for disaster in disasters:
            if disaster.type in self.lasting_disasters:
                total += 1
        return total
