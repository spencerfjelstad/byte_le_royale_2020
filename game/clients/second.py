from game.client.user_client import UserClient
from game.utils.oop import *

import sys

class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()

    def team_name(self):
        return "Communist Russia"

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions, city, disasters):
        actions.add_effort("Mandatory labor for everyone", sys.maxsize)

    def set_decree(self, my_decree):
        return "everyone to the gulag"
