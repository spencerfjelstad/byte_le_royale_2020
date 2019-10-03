from game.controllers.controller import Controller
from game.controllers.event_controller import EventController
from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.player import Player


class DisasterController(Controller):
    def __init__(self):
        super().__init__()
        self.debug = True
        self.event_controller = EventController.get_instance()

    def handle_actions(self, player):

        remaining_disasters = list()
        for dis in player.disasters:
            if dis.status == DisasterStatus.dead:
                # Disaster is dead, remove from the list
                self.event_controller.add_event({
                    "event_type": EventType.disaster_eliminated,
                    "disaster": dis.to_json(),
                })
            else:
                # Disaster is still alive
                remaining_disasters.append(dis)

        player.disasters = remaining_disasters
