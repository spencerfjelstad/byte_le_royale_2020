import unittest
import io
import sys
from game.controllers import *


class TestControllerInheritance(unittest.TestCase):

    def setUp(self):
        self.test_disaster_controller = DisasterController()
        self.test_economy_controller = EconomyController()
        self.test_sensor_controller = SensorController()

    def test_debug_false(self):
        self.test_disaster_controller.debug = False
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            self.test_disaster_controller.log("Hello There!")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "")
        finally:
            sys.stdout = saved_stdout

    def test_debug_true(self):
        self.test_disaster_controller.debug = True
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            self.test_disaster_controller.log("General Kenobi.")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "General Kenobi.")
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
