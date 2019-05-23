import unittest
from game.common.disasters import *


class TestDisasterObjects(unittest.TestCase):

    def test_init(self):
        my_fire = Fire()
        self.assertIsInstance(my_fire, Fire)
        self.assertIsInstance(my_fire, LastingDisaster)
        self.assertIsInstance(my_fire, Disaster)

    def test_abstract_init_fail(self):
        self.assertRaises(TypeError, lambda: LastingDisaster())

    def test_abstract_init_fail_2(self):
        self.assertRaises(TypeError, lambda: Disaster())


if __name__ == '__main__':
    unittest.main()
