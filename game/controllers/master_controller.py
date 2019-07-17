from copy import deepcopy

from game.common.enums import *
from game.common.player import Player
from game.common.action import Action
from game.common.disasters import *
from game.common.city import City
from game.config import *

from game.controllers.controller import Controller
from game.controllers.destruction_controller import DestructionController
from game.controllers.sensor_controller import SensorController


class MasterController(Controller):
    def __init__(self):
        super().__init__()

        self.destructionController = DestructionController()
        self.sensorController = SensorController()

        self.game_over = False

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, client):
        client.city = City()
        client.team_name = client.code.team_name()

    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, client, world, turn):
        # Turn disaster occurrence into a real disaster
        for disaster in world['disasters']:
            dis = None
            if disaster is DisasterType.earthquake:
                dis = Earthquake()
            elif disaster is DisasterType.fire:
                dis = Fire()
            elif disaster is DisasterType.hurricane:
                dis = Hurricane()
            elif disaster is DisasterType.monster:
                dis = Monster()
            elif disaster is DisasterType.tornado:
                dis = Tornado()
            elif disaster is DisasterType.ufo:
                dis = Ufo()

            if dis is None:
                raise TypeError(f'Attempt to create disaster failed because given type: {disaster}, does not exist.')

            client.disasters.append(dis)

        world['rates'] = {int(key): val for key, val in world['rates'].items()}
        # Calculate error ranges
        self.sensorController.calculate_turn_ranges(turn, world['rates'])
        sensor_estimates = self.sensorController.turn_ranges[turn]

        # give clients their corresponding sensor odds
        sensor_results = dict()
        for sensor, level in client.city.sensors.items():
            sensor_results[sensor] = sensor_estimates[sensor][level]
        client.city.sensor_results = sensor_results

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def clients_turn_arguments(self, client, world, turn):
        actions = Action()
        client.action = actions

        obfuscated_city = client.city
        obfuscated_disasters = client.disasters

        args = (actions, obfuscated_city, obfuscated_disasters,)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, client, world, turn):
        self.destructionController.handle_actions(client)

        if client.city.structure <= 0 or client.city.population <= 0:
            self.game_over = True

    # Return serialized version of game
    def create_turn_log(self, client, world, turn):
        data = dict()
        data['rates'] = world['rates']
        data['players'] = list()
        data['players'].append(client.to_json())

        return data

    # Return if the game should be over
    def game_over_check(self):
        return self.game_over
