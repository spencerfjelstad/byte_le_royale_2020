from collections import deque

from game.config import *
from game.common.enums import *


class Action:
    def __init__(self):
        self._allocation_list = deque(maxlen=MAX_ALLOCATIONS_ALLOWED_PER_TURN)
        self._decree = None

    def add_effort(self, effort, number):
        # TODO enforce input to match a standard
        self._allocation_list.append([effort, number])

    def set_decree(self, dec):
        # TODO enforce input to match a standard
        self._decree = dec

    def to_json(self):
        res = dict()
        res['effort'] = list(self._allocation_list)
        res['decree'] = self._decree
        return res
