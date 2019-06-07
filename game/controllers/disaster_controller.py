from game.controllers import Controller
from game.common.disasters import *


class DisasterController(Controller):

    @staticmethod
    def reduce_disaster(effort, disaster):

        if not isinstance(disaster, LastingDisaster):
            return

        if effort < 0:
            return

        disaster.reduce(effort)
