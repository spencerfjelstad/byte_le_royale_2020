import unittest

from game.common.enums import *
from game.controllers import SensorController


class TestSensors(unittest.TestCase):

    def setUp(self):
        self.test_sensor_controller = SensorController()

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
