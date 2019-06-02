import unittest
import io
import sys
from game.controllers import *


class TestControllerInheritance(unittest.TestCase):

    def setUp(self):
        Controller.debug = False
        EconomyController.debug = False

    def tearDown(self):
        Controller.debug = False
        EconomyController.debug = False

    def test_debug_false(self):
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            Controller.log("Hello There!")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "")
        finally:
            sys.stdout = saved_stdout

    def test_debug_true(self):
        EconomyController.debug = True
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            EconomyController.log("General Kenobi.")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "General Kenobi.")
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
