import unittest

from game.common.enums import *
from game.common.action import Action
from game.common.city import City
from game.common.player import Player
from game.utils.generate_game import calculate_sensor_ranges
from game.controllers.effort_controller import EffortController


class TestSensors(unittest.TestCase):

    def setUp(self):
        self.test_effort_controller = EffortController()

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
        turn_ranges = dict()
        for turn in range(100):
            turn_ranges[turn] = calculate_sensor_ranges(test_odds)

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

        self.assertEqual(fire_sensor.level, SensorLevel.level_zero)

        player.action.add_effort(fire_sensor, 50)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.level, SensorLevel.level_one)

        player.action = Action()
        player.action.add_effort(fire_sensor, 100)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.level, SensorLevel.level_two)

        player.action = Action()
        player.action.add_effort(fire_sensor, 500)
        self.test_effort_controller.handle_actions(player)
        self.assertEqual(fire_sensor.level, SensorLevel.level_three)
