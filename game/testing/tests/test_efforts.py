import unittest
from game.common.action import Action
from game.common.city import City
from game.common.disasters.fire import Fire
from game.common.disasters.hurricane import Hurricane
from game.common.disasters.monster import Monster
from game.common.player import Player
from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.effort_controller import EffortController
from game.controllers.disaster_controller import DisasterController
from game.controllers.sensor_controller import SensorController
from game.utils.helpers import enum_iter


class TestEfforts(unittest.TestCase):

    def setUp(self):
        self.test_effort_controller = EffortController()
        self.test_disaster_controller = DisasterController()
        self.test_sensor_controller = SensorController()
        self.controllers = {
            "sensor": self.test_sensor_controller,
            "disaster": self.test_disaster_controller,
            "effort": self.test_effort_controller
        }
        self.test_effort_controller.import_controllers(self.controllers)
        self.player = Player()
        self.player.action = Action()
        self.player.city = City()

    def test_sensor(self):
        TEST_SENSOR_AMOUNT = 1
        for sensor_type in enum_iter(SensorType):
            self.player.action.add_effort(self.player.city.sensors[sensor_type], TEST_SENSOR_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        for sensor in self.player.city.sensors.values():
            self.assertEqual(sensor.sensor_effort_remaining,
                             GameStats.sensor_effort[SensorLevel.level_one] - TEST_SENSOR_AMOUNT)

    def test_disaster(self):
        TEST_DISASTER_AMOUNT = 1
        test_disaster_list = list()
        for dis in {Fire(), Hurricane(), Monster()}:
            test_disaster_list.append(dis)
            self.player.disasters.append(dis)

        for dis in test_disaster_list:
            self.player.action.add_effort(dis, TEST_DISASTER_AMOUNT)

        self.test_effort_controller.handle_actions(self.player)
        for dis in test_disaster_list:
            self.assertEqual(dis.effort_remaining,
                             GameStats.disaster_initial_efforts[dis.type] - TEST_DISASTER_AMOUNT)

