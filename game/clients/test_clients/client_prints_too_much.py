from game.client.user_client import UserClient
from game.utils.oop import *
from game.common.enums import *

import random
import sys

class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()

    @overrides(UserClient)
    def team_name(self):
        return "Team Superior_Debugging"

    @overrides(UserClient)
    def city_name(self):
        print("we gotta come up with a good team name...")
        return "let_me_think-ville"

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions, city, disasters):
        for _ in range(10):
            print(random.choice(["Hmm...", "I wonder...", "Maybe...", "or possibly...?", "We could..."]))

        # do stuff here
        print("that should work")
        pass
    @overrides(UserClient)
    def set_decree(self, my_decree):
        return "everyone to the gulag"
