import io
import unittest
import sys

from game.controllers.event_controller import EventController
from game.controllers.singleton_controller import SingletonController


class TestSingleton(unittest.TestCase):

    def setUp(self):
        EventController._instance = None
        SingletonController._instance = None

    # generate an instance of singleton controller
    def test_generate(self):
        EventController()
        SingletonController()

    # get an instance of singleton controller after generation
    def test_get(self):
        test_ec = EventController()
        test_sc = SingletonController()

        self.assertEqual(test_ec, EventController.get_instance())
        self.assertEqual(test_sc, SingletonController.get_instance())

    # Ensures the message received properly inherits and doesn't use the abstract class's message
    def test_message(self):
        capture_output = io.StringIO()
        saved_stdout = sys.stdout
        try:
            sys.stdout = capture_output
            EventController()
            EventController()
            actual_message = capture_output.getvalue().strip()
            self.assertEqual(actual_message,
                             "EventController is a singleton and has already been instantiated. "
                             "Use EventController.get_instance() to get instance of the class."
                             )
        finally:
            sys.stdout = saved_stdout
