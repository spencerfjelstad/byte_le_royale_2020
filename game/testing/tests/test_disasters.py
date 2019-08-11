import unittest

from game.controllers.disaster_controller import DisasterController
from game.common.action import Action
from game.common.city import City
from game.common.disasters.fire import Fire
from game.common.disasters.hurricane import Hurricane
from game.common.disasters.monster import Monster
from game.common.enums import *
from game.common.player import Player
from game.common.stats import GameStats

class TestDisasters(unittest.TestCase):

    def setUp(self):
        self.test_disaster_controller = DisasterController()

    def test_reduce(self):
        # Setup
        player = Player()
        player.action = Action()
        player.city = City()

        # Create disasters
        test_disaster_list = list()
        for dis in {Fire(), Hurricane(), Monster()}:
            test_disaster_list.append(dis)
            player.disasters.append(dis)

        # Have player handle disasters
        for dis in player.disasters:
            if isinstance(dis, Fire):
                player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.fire])
            if isinstance(dis, Hurricane):
                player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.hurricane])
            if isinstance(dis, Monster):
                player.action.add_effort(dis, GameStats.disaster_initial_efforts[DisasterType.monster])

        # Unhandled fire addition
        unhandled_fire = Fire()
        test_disaster_list.append(unhandled_fire)
        player.disasters.append(unhandled_fire)

        # Run controller
        self.test_disaster_controller.handle_actions(player)

        # Test outcome
        for dis in test_disaster_list:
            if dis == unhandled_fire:
                self.assertEqual(dis.effort_remaining, GameStats.disaster_initial_efforts[DisasterType.fire])
                self.assertEqual(dis.status, DisasterStatus.live)
                self.assertIn(dis, player.disasters)
            else:
                self.assertEqual(dis.effort_remaining, 0)
                self.assertEqual(dis.status, DisasterStatus.dead)
                self.assertNotIn(dis, player.disasters)
