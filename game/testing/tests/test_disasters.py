import unittest

from game.common.action import Action
from game.common.city import City
from game.common.disasters.fire import Fire
from game.common.disasters.hurricane import Hurricane
from game.common.disasters.monster import Monster
from game.common.enums import *
from game.common.player import Player
from game.common.stats import GameStats
from game.controllers.disaster_controller import DisasterController
from game.controllers.effort_controller import EffortController


class TestDisasters(unittest.TestCase):

    def setUp(self):
        # Setup
        self.test_disaster_controller = DisasterController()
        self.test_effort_controller = EffortController()
        self.player = Player()
        self.player.action = Action()
        self.player.city = City()

    def test_reduce(self):
        # Create disasters
        test_disaster_list = list()
        for dis in {Fire(), Hurricane(), Monster()}:
            test_disaster_list.append(dis)
            self.player.disasters.append(dis)

        # Have player handle disasters
        for dis in self.player.disasters:
            if isinstance(dis, Fire):
                self.player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.fire])
            if isinstance(dis, Hurricane):
                self.player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.hurricane])
            if isinstance(dis, Monster):
                self.player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.monster])

        # Unhandled fire addition
        unhandled_fire = Fire()
        test_disaster_list.append(unhandled_fire)
        self.player.disasters.append(unhandled_fire)

        # Run controllers
        self.test_effort_controller.handle_actions(self.player)
        self.test_disaster_controller.handle_actions(self.player)

        # Test outcome
        for dis in test_disaster_list:
            if dis == unhandled_fire:
                self.assertEqual(dis.effort_remaining, GameStats.disaster_initial_efforts[DisasterType.fire])
                self.assertEqual(dis.status, DisasterStatus.live)
                self.assertIn(dis, self.player.disasters)
            else:
                self.assertEqual(dis.effort_remaining, 0)
                self.assertEqual(dis.status, DisasterStatus.dead)
                self.assertNotIn(dis, self.player.disasters)
