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
