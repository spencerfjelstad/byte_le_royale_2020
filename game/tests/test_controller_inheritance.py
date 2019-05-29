import unittest
from game.controllers import *


class TestControllerInheritance(unittest.TestCase):

    def setUp(self):
        EconomyController.del_instance()

    def test_abstract_init_fail(self):
        self.assertRaises(TypeError, lambda: Controller())

    def test_get_instance(self):
        my_econ_controller = EconomyController()
        my_same_controller = EconomyController.get_instance()
        self.assertEqual(my_econ_controller, my_same_controller)

    def test_init(self):
        EconomyController()

    def test_warning(self):
        EconomyController()
        self.assertWarns(UserWarning, lambda: EconomyController())


if __name__ == '__main__':
    unittest.main()
