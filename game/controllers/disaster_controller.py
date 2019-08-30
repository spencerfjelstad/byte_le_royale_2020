from game.controllers.controller import Controller
from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.player import Player


class DisasterController(Controller):
    def __init__(self):
        super().__init__()
        self.debug = True

    def handle_actions(self, player):
        # Remove any dead disasters from the disaster list
        player.disasters = [dis for dis in player.disasters if not dis.status == DisasterStatus.dead]

    def reduce_disaster(self, player, lasting_disaster, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(lasting_disaster, LastingDisaster):
            self.print("The lasting_disaster argument is not a LastingDisaster object.")
            return
        if lasting_disaster.status != DisasterStatus.live:
            self.print("Disaster has already been stopped.")
            return

        lasting_disaster.reduce(number)