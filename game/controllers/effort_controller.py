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

from collections import deque
import math


class EffortController(Controller):
    def __init__(self):
        super().__init__()
        self.event_controller = EventController.get_instance()

    def handle_actions(self, player):
        # handle advanced verification of allocation list
        player.city.remaining_man_power = player.city.population
        allocations = dict()  # condensed duplicate entries
        player_actions = self.__reverse_obfuscation(player)
        for allocation in player_actions:
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
                self.apply_upgrade_effort(player, act, amount)
            elif isinstance(act, City):
                self.apply_upgrade_effort(player, act, amount)
            elif isinstance(act, LastingDisaster):
                self.apply_disaster_effort(player, act, amount)
            elif isinstance(act, Sensor):
                self.apply_upgrade_effort(player, act, amount)
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
                    self.apply_upgrade_effort(player, player.city, amount)
                else:
                    raise NotImplementedError(f"Effort towards this ActionType ({act}) is not yet implemented. "
                                              f"Open an issue if this ActionType should have been implemented.")
            else:
                raise ValueError(f"Player {player} allocated amount {amount} towards illegal target {act}. "
                                 "Validation should have prevented this.")

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

    # Upgrades a building, city, or sensor given inputted effort (and available wealth, for buildings)
    def apply_upgrade_effort(self, player, obj, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(obj, (Building, City, Sensor)):
            self.print("The object argument is not a valid upgradable object.")
            return
        if isinstance(obj, Building) and obj not in player.city.buildings.values():
            self.print("Building is not a part of the city.")
            self.print("Building: {}".format(obj))
            for building in player.city.buildings:
                self.print("City buildings: {}".format(building))
            return
        if isinstance(obj, Sensor) and obj not in player.city.sensors.values():
            self.print("Sensor is not a part of the city.")
            self.print("Sensor: {}".format(obj))
            for sens in player.city.sensors:
                self.print("City sensor: {}".format(sens))
            return

        # Repeat as long as there is effort remaining left to allocate. This loops
        # so that allocating effort past the current level requirement will go towards the level after
        while number > 0:
            current_level = obj.level
            next_level = None
            level_after = None

            # Find the next level requirement (based on current level and object type)
            if isinstance(obj, Building):
                if current_level == BuildingLevel.level_zero:
                    next_level = BuildingLevel.level_one
                    level_after = None
                elif current_level == BuildingLevel.level_one:
                    self.print("Building level is already maxed.")
                    obj.effort_remaining = 0
                    return
                else:
                    self.print("building's level value is invalid.")
                    return
            elif isinstance(obj, City):
                if current_level == CityLevel.level_zero:
                    next_level = CityLevel.level_one
                    level_after = CityLevel.level_two
                elif current_level == CityLevel.level_one:
                    next_level = CityLevel.level_two
                    level_after = CityLevel.level_three
                elif current_level == CityLevel.level_two:
                    next_level = CityLevel.level_three
                    level_after = None
                elif current_level == CityLevel.level_three:
                    self.print("City level is already maxed.")
                    obj.effort_remaining = 0
                    return
                else:
                    self.print("City's level value is invalid.")
                    return
            elif isinstance(obj, Sensor):
                if current_level == SensorLevel.level_zero:
                    next_level = SensorLevel.level_one
                    level_after = SensorLevel.level_two
                elif current_level == SensorLevel.level_one:
                    next_level = SensorLevel.level_two
                    level_after = SensorLevel.level_three
                elif current_level == SensorLevel.level_two:
                    next_level = SensorLevel.level_three
                    level_after = None
                elif current_level == SensorLevel.level_three:
                    self.print("Sensor level is already maxed.")
                    obj.effort_remaining = 0
                    return
                else:
                    self.print("sensor's sensor_level value is invalid.")
                    return

            # Reduce the number down to what the city's wealth will permit (for building upgrades)
            if isinstance(obj, Building):
                number = clamp(number, min_value=0, max_value=player.city.gold)
                player.city.gold -= number

            # Move all the effort from number to the upgradable object
            obj.effort_remaining -= number

            number = 0  # For now, set number to 0. If there's left over allocation, we pull it back from the object

            # if limit maxed, begin upgrade
            if obj.effort_remaining <= 0:
                self.print(f"Object {obj} has leveled up! Level {next_level} reached.")

                # apply changes
                left_over = obj.effort_remaining * -1  # reverse, because effort allocation must be positive

                event_type = None
                if isinstance(obj, Building):
                    if level_after is not None:
                        obj.effort_remaining = GameStats.building_upgrade_cost[obj.building_type][level_after]
                    else:
                        obj.effort_remaining = 0
                    event_type = EventType.building_upgrade
                elif isinstance(obj, City):
                    obj.max_structure = GameStats.city_max_structure[next_level]
                    if level_after is not None:
                        obj.effort_remaining = GameStats.city_upgrade_cost[level_after]
                    else:
                        obj.effort_remaining = 0
                    event_type = EventType.city_upgrade
                elif isinstance(obj, Sensor):
                    if level_after is not None:
                        obj.effort_remaining = GameStats.sensor_upgrade_cost[level_after]
                    else:
                        obj.effort_remaining = 0
                    event_type = EventType.sensor_upgrade
                obj.level = next_level

                # log upgrade
                self.event_controller.add_event({
                    "event_type": event_type,
                    "upgraded object": obj.to_json(),
                })

                # with left over effort, attempt upgrade again
                number = left_over

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

    def __reverse_obfuscation(self, player):
        new_actions = list()
        for allocation in player.action.get_allocation_list():
            act, amount = allocation
            if isinstance(act, Building):
                server_obj = [bldg for bldg in player.city.buildings.values() if bldg.building_type == act.building_type][0]
            elif isinstance(act, City):
                server_obj = player.city
            elif isinstance(act, LastingDisaster):
                server_obj = [dis for dis in player.disasters if dis.id == act.id][0]
            elif isinstance(act, Sensor):
                server_obj = [sens for sens in player.city.sensors.values() if sens.sensor_type == act.sensor_type][0]
            else:
                # object doesn't need reversing
                server_obj = act
            new_actions.append([server_obj, amount])
        return new_actions

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
