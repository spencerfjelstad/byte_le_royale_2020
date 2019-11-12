from game.common.stats import GameStats
from game.common.building import Building
from game.common.city import City
from game.common.disasters import LastingDisaster
from game.common.player import Player
from game.common.sensor import Sensor
from game.controllers.controller import Controller
from game.controllers.event_controller import EventController
from game.config import *
from game.utils.helpers import clamp, enum_iter

import math


class EffortController(Controller):
    def __init__(self):
        super().__init__()
        self.event_controller = EventController.get_instance()

    def handle_actions(self, player):
        # handle advanced verification of allocation list
        player.city.remaining_man_power = player.city.population
        allocations = dict()  # condensed duplicate entries

        for allocation in player.action.get_allocation_list():
            act, amount = allocation

            # Do any additional, server side action validation here

            # Skip action (no man power left)
            if player.city.remaining_man_power == 0:
                self.print("All man power exhausted. Skipping allocation: {}".format(allocation))
                continue

            # Reduce requested amount to maximum remaining
            if amount > player.city.remaining_man_power:
                self.print("Too much man power requested for action. Reducing to remaining man power.")
                amount = player.city.remaining_man_power

            # Reduce man power
            player.city.remaining_man_power -= amount

            # Save action
            if act not in allocations:
                allocations[act] = 0
            allocations[act] += amount

        # Convert the allocations into a sortable list
        allocations = sorted(allocations.items(), key=EffortController.__sort_allocations)

        # Handle control of efforts here
        for act, amount in allocations:
            if isinstance(act, Building):
                self.apply_building_effort(player, act, amount)
            elif isinstance(act, City):
                self.apply_city_effort(player, amount)
            elif isinstance(act, LastingDisaster):
                self.apply_disaster_effort(player, act, amount)
            elif isinstance(act, Sensor):
                self.apply_sensor_effort(player, act, amount)
            elif act in enum_iter(ActionType):
                if act == ActionType.none:
                    self.apply_no_effort(player, amount)
                elif act == ActionType.repair_structure:
                    self.apply_structure_effort(player, amount)
                elif act == ActionType.regain_population:
                    self.apply_population_effort(player, amount)
                elif act == ActionType.accumulate_wealth:
                    self.apply_wealth_effort(player, amount)
                elif act == ActionType.upgrade_city:
                    self.apply_city_effort(player, amount)
                else:
                    raise NotImplementedError(f"Effort towards this ActionType ({act}) is not yet implemented. "
                                              f"Open an issue if this ActionType should have been implemented.")
            else:
                raise ValueError(f"Player {player} allocated amount {amount} towards illegal target {act}. "
                                 "Validation should have prevented this.")

    # Puts work towards upgrading a building for various effects
    def apply_building_effort(self, player, building, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(building, Building):
            self.print("The sensor argument is not a Sensor object.")
            return
        if building not in player.city.buildings.values():
            self.print("Building is not a part of the city.")
            self.print("Building: {}".format(building))
            for building in player.city.buildings:
                self.print("City buildings: {}".format(building))
            return

        while number > 0:
            if building.building_level == BuildingLevel.level_three:
                self.print("Building level is already maxed.")
                return

            current_level = building.building_level
            if current_level == BuildingLevel.level_zero:
                next_level = BuildingLevel.level_one
            elif current_level == BuildingLevel.level_one:
                next_level = BuildingLevel.level_two
            elif current_level == BuildingLevel.level_two:
                next_level = BuildingLevel.level_three
            else:
                self.print("building's building_level value is invalid.")
                return

            # Move all the effort from number to the building
            building.effort_remaining -= number
            number = 0  # For now, set number to 0. If there's left over allocation, we pull it back from the sensor

            # if limit maxed, begin upgrade
            if building.effort_remaining <= 0:
                self.print(f"Building level {next_level} reached!")
                # apply changes
                left_over = building.effort_remaining * -1  # reverse, because effort allocation must be positive
                building.effort_remaining = GameStats.building_effort[next_level]
                building.building_level = next_level

                # log upgrade
                self.event_controller.add_event({
                    "event_type": EventType.sensor_upgrade,
                    "building": building.to_json(),
                })

                # with left over effort, attempt upgrade again
                number = left_over

    # Puts work towards upgrading the city to increase max structure amount
    def apply_city_effort(self, player, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return

        while number > 0:
            if player.city.level == CityLevel.level_two:
                self.print("City level is already maxed.")
                return

            current_level = player.city.level
            if current_level == CityLevel.level_zero:
                next_level = CityLevel.level_one
            elif current_level == CityLevel.level_one:
                next_level = CityLevel.level_two
            else:
                self.print("City's level value is invalid.")
                return

            # Move all the effort from number to the city
            player.city.effort_until_upgrade -= number
            number = 0  # For now, set number to 0. If there's left over allocation, we pull it back from the city

            # if limit maxed, begin upgrade
            if player.city.effort_until_upgrade <= 0:
                self.print(f"City level {next_level} reached!")

                # apply changes
                left_over = player.city.effort_until_upgrade * -1  # reverse, because effort allocation must be positive
                player.city.effort_until_upgrade = GameStats.city_upgrade_cost[next_level]
                player.city.level = next_level

                # log upgrade
                self.event_controller.add_event({
                    "event_type": EventType.city_upgrade,
                    "city": player.city.to_json(),
                })

                # with left over effort, attempt upgrade again
                number = left_over

    # Reduces disaster life when effort is applied
    def apply_disaster_effort(self, player, lasting_disaster, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(lasting_disaster, LastingDisaster):
            self.print("The lasting_disaster argument is not a LastingDisaster object.")
            return
        if lasting_disaster.status != DisasterStatus.live:
            self.print("Disaster has already been stopped.")
            return

        lasting_disaster.reduce(number)

    def apply_no_effort(self, player, number):
        if number > 0:
            self.print(f"{number} population allocated towards ActionType.none by player {player}. "
                       f"Are you sure the population should be doing nothing?")

    # Increase population level given effort
    def apply_population_effort(self, player, number):
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return

        # Apply an effectiveness multiplier here
        increase = math.floor(number * GameStats.effort_population_multiplier)
        # Update population without going over structure
        player.city.population = clamp(player.city.population+increase, min_value=0, max_value=player.city.structure)

    # Upgrades sensors when effort is applied
    def apply_sensor_effort(self, player, sensor, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(sensor, Sensor):
            self.print("The sensor argument is not a Sensor object.")
            return
        if sensor not in player.city.sensors.values():
            self.print("Sensor is not a part of the city.")
            self.print("Sensor: {}".format(sensor))
            for sens in player.city.sensors:
                self.print("City sensor: {}".format(sens))
            return

        while number > 0:
            if sensor.sensor_level == SensorLevel.level_three:
                self.print("Sensor level is already maxed.")
                return

            current_level = sensor.sensor_level
            if current_level == SensorLevel.level_zero:
                next_level = SensorLevel.level_one
            elif current_level == SensorLevel.level_one:
                next_level = SensorLevel.level_two
            elif current_level == SensorLevel.level_two:
                next_level = SensorLevel.level_three
            else:
                self.print("sensor's sensor_level value is invalid.")
                return

            # Move all the effort from number to the city
            sensor.sensor_effort_remaining -= number
            number = 0  # For now, set number to 0. If there's left over allocation, we pull it back from the sensor

            # if limit maxed, begin upgrade
            if sensor.sensor_effort_remaining <= 0:
                self.print(f"Sensor level {next_level} reached!")
                # apply changes
                left_over = sensor.sensor_effort_remaining * -1  # reverse, because effort allocation must be positive
                sensor.sensor_effort_remaining = GameStats.sensor_effort[next_level]
                sensor.sensor_level = next_level

                # log upgrade
                self.event_controller.add_event({
                    "event_type": EventType.sensor_upgrade,
                    "sensor": sensor.to_json(),
                })

                # with left over effort, attempt upgrade again
                number = left_over

    def apply_structure_effort(self, player, number):
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return

        # Apply an effectiveness multiplier here
        increase = math.floor(number * GameStats.effort_structure_multiplier)

        # Update population without going over structure
        player.city.structure = clamp(player.city.structure+increase, min_value=0, max_value=player.city.max_structure)

    def apply_wealth_effort(self, player, number):
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return

        # Apply an effectiveness multiplier here
        increase = math.floor(number * GameStats.effort_gold_multiplier)

        player.city.gold += increase

        raise NotImplementedError

    # Sorts the allocations in order they should be processed
    # e.g. homes (structure) should be repaired before new people (population) are generated
    @staticmethod
    def __sort_allocations(allocation):
        act, amount = allocation
        try:
            if act in enum_iter(ActionType):
                return GameStats.action_sort_order[act]
            else:
                return GameStats.object_sort_order[act.object_type]
        except KeyError as e:
            print("SYSTEM EXCEPTION: Game object passed to the allocation list was not included in the sort order.")
            print("If you are receiving this error, please let Wyly know.")
            raise e
