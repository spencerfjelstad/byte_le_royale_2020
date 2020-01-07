import math
import unittest
from game.common.action import Action
from game.common.city import City
from game.common.disasters.fire import Fire
from game.common.disasters.blizzard import Blizzard
from game.common.disasters.monster import Monster
from game.common.player import Player
from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.effort_controller import EffortController
from game.controllers.disaster_controller import DisasterController
from game.utils.helpers import enum_iter


class TestEfforts(unittest.TestCase):

    def setUp(self):
        self.test_effort_controller = EffortController()
        self.test_disaster_controller = DisasterController()
        self.player = Player()
        self.player.action = Action()
        self.player.city = City()

    def test_city(self):
        TEST_CITY_AMOUNT = 1
        self.player.action.add_effort(self.player.city, TEST_CITY_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        self.assertEqual(self.player.city.effort_remaining,
                         GameStats.city_upgrade_cost[CityLevel.level_one] - TEST_CITY_AMOUNT)

    def test_sensor(self):
        TEST_SENSOR_AMOUNT = 1
        for sensor_type in enum_iter(SensorType):
            self.player.action.add_effort(self.player.city.sensors[sensor_type], TEST_SENSOR_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        for sensor in self.player.city.sensors.values():
            self.assertEqual(sensor.effort_remaining,
                             GameStats.sensor_upgrade_cost[SensorLevel.level_one] - TEST_SENSOR_AMOUNT)

    def test_population(self):
        TEST_POPULATION_AMOUNT = 20
        self.player.city.population = 50
        self.player.action.add_effort(ActionType.regain_population, TEST_POPULATION_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        self.assertEqual(self.player.city.population,
                         math.floor(GameStats.effort_population_multiplier * TEST_POPULATION_AMOUNT) + 50)

    def test_structure(self):
        TEST_STRUCTURE_AMOUNT = 20
        self.player.city.structure = 0
        self.player.action.add_effort(ActionType.repair_structure, TEST_STRUCTURE_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        self.assertEqual(self.player.city.structure,
                         math.floor(GameStats.effort_structure_multiplier * TEST_STRUCTURE_AMOUNT))

    def test_disaster(self):
        TEST_DISASTER_AMOUNT = 1
        test_disaster_list = list()
        for dis in {Fire(), Blizzard(), Monster()}:
            test_disaster_list.append(dis)
            self.player.disasters.append(dis)

        for dis in test_disaster_list:
            self.player.action.add_effort(dis, TEST_DISASTER_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        for dis in test_disaster_list:
            self.assertEqual(dis.effort_remaining,
                             GameStats.disaster_initial_efforts[dis.type] - TEST_DISASTER_AMOUNT)

