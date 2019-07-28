from game.controllers.controller import Controller
from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.player import Player


class DisasterController(Controller):
    def __init__(self):
        super().__init__()
        self.debug = True

    def handle_actions(self, player):
        # Handle effort allocation for disasters
        for act in player.action._allocation_list:
            effort, number = act
            if isinstance(effort, LastingDisaster):
                self.__reduce_disaster(player, effort, number)

        # Remove any dead disasters from the disaster list
        player.disasters = [dis for dis in player.disasters if not dis.status == DisasterStatus.dead]

    def __reduce_disaster(self, player, lasting_disaster, number):
        # Validate input
        if number < 0:
            self.log("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.log("The player argument is not a Player object.")
            return
        if not isinstance(lasting_disaster, LastingDisaster):
            self.log("The lasting_disaster argument is not a LastingDisaster object.")
            return
        if lasting_disaster.status != DisasterStatus.live:
            self.log("Disaster has already been stopped.")
            return

        lasting_disaster.reduce(number)