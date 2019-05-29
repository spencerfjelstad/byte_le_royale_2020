import unittest
from game.common.disasters import *


class TestDisasterObjects(unittest.TestCase):

    #  Fire Object Testing

    def test_init_fire(self):
        my_fire = Fire()
        self.assertIsInstance(my_fire, Fire)
        self.assertIsInstance(my_fire, LastingDisaster)
        self.assertIsInstance(my_fire, Disaster)

    def test_abstract_init_fire_fail(self):
        self.assertRaises(TypeError, lambda: LastingDisaster())

    def test_abstract_init_fire_fail_2(self):
        self.assertRaises(TypeError, lambda: Disaster())

    
    #  Tornado Object Testing

    #def test_init_tornado(self):
    #    my_tornado = Tornado()
    #    self.assertIsInstance(my_tornado, Tornado)
    #    self.assertIsInstance(my_tornado, Disaster)


if __name__ == '__main__':
    unittest.main()
