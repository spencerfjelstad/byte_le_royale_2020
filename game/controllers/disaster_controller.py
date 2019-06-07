from game.controllers import Controller
from game.common.disasters import *


class DisasterController(Controller):

    @classmethod
    def reduce_disaster(cls, effort, disaster):

        if not isinstance(disaster, Disaster):
            cls.log("given disaster is not a Disaster object.")
        if not isinstance(disaster, LastingDisaster):
            cls.log("Given disaster is not a LastingDisaster object.")
            return

        if effort < 0:
            cls.log("Given effort is not positive.")
            return

        disaster.reduce(effort)
        cls.log("Disaster has been reduced.")
