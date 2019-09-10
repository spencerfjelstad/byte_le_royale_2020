import unittest

from game.common.enums import *
from game.common.action import Action
from game.common.city import City
from game.common.player import Player

from game.controllers.effort_controller import EffortController
from game.controllers.sensor_controller import SensorController


class TestSensors(unittest.TestCase):

    def setUp(self):
        self.test_effort_controller = EffortController()
        self.test_sensor_controller = SensorController()
        self.controllers = {
            "effort": self.test_effort_controller,
            "sensor": self.test_sensor_controller
        }
        self.test_effort_controller.import_controllers(self.controllers)

    def test_double_generate_fail(self):
        test_odds = {
            DisasterType.fire: 0.3,
            DisasterType.tornado: 0.2,
            DisasterType.hurricane: 0.14,
            DisasterType.earthquake: 0.29,
            DisasterType.monster: 0.9,
            DisasterType.ufo: 0.1
        }

        self.test_sensor_controller.calculate_turn_ranges(turn=1, odds=test_odds)

        self.assertRaises(ValueError,
                          lambda: self.test_sensor_controller.calculate_turn_ranges(turn=1, odds=test_odds))

    # Note: not a guaranteed success rate
    def test_legal_odds(self):
        test_odds = {
            DisasterType.fire: 0.0,
            DisasterType.tornado: 0.5,
            DisasterType.hurricane: 0.99,
            DisasterType.earthquake: 1.00,
            DisasterType.monster: 1.00,
            DisasterType.ufo: 0.0
        }
        for turn in range(10000):
            self.test_sensor_controller.calculate_turn_ranges(turn, test_odds)
        turn_ranges = self.test_sensor_controller.turn_ranges

        max_val = -0.01
        min_val = 1.01
        for sensors in turn_ranges.values():
            for level in sensors.values():
                for val in level.values():
                    if val > max_val:
                        max_val = val
                    if val < min_val:
                        min_val = val
        self.assertGreaterEqual(1, max_val)
        self.assertLessEqual(0, min_val)

    def test_upgrade(self):
        # Setup
        player = Player()
        player.action = Action()
        player.city = City()
        fire_sensor = player.city.sensors[SensorType.fire_alarm]

        self.assertEqual(fire_sensor.sensor_level, SensorLevel.level_zero)

        player.action.add_effort(fire_sensor, 50)
        self.test_sensor_controller.handle_actions(player)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.sensor_level, SensorLevel.level_one)

        player.action = Action()
        player.action.add_effort(fire_sensor, 100)
        self.test_sensor_controller.handle_actions(player)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.sensor_level, SensorLevel.level_two)

        player.action = Action()
        player.action.add_effort(fire_sensor, 500)
        self.test_sensor_controller.handle_actions(player)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.sensor_level, SensorLevel.level_three)
