import unittest
import io
import sys
from game.controllers.controller import Controller
from game.controllers.destruction_controller import DestructionController
from game.controllers.disaster_controller import DisasterController
from game.controllers.master_controller import MasterController
from game.common.enums import *


class TestControllerInheritance(unittest.TestCase):

    def setUp(self):
        self.test_destruction_controller = DestructionController()
        self.test_disaster_controller = DisasterController()
        self.test_master_controller = MasterController()

#    # No longer works, ABC inheritance removed
#    def test_abstract_init_fail(self):
#        self.assertRaises(TypeError, lambda: Controller())

    def test_debug_false(self):
        self.test_disaster_controller.debug = False
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            self.test_disaster_controller.print("Hello There!")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "")
        finally:
            sys.stdout = saved_stdout

    def test_debug_true(self):
        self.test_disaster_controller.debug = True
        self.test_disaster_controller.debug_level = DebugLevel.none
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            self.test_disaster_controller.print("General Kenobi.")
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message, "DisasterController: General Kenobi.")
        finally:
            sys.stdout = saved_stdout

    def test_inheritance(self):
        self.assertIsInstance(self.test_destruction_controller, Controller)
        self.assertIsInstance(self.test_disaster_controller, Controller)
        self.assertIsInstance(self.test_master_controller, Controller)


if __name__ == '__main__':
    unittest.main()
