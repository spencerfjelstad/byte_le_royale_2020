from game.client.user_client import UserClient
from game.utils.oop import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()
        self.number = 100

    def team_name(self):
        return "crungy bungus"

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions, city, disasters):
        #while True:
        #    actions.add_effort("heehee i'm overflowing memory :)", 1)
        actions.add_effort("heehee i'm not doing anything actually", 1)
        actions.add_effort("other action to make it look not funny in the logs", 1093)

    def set_decree(self, my_decree):
        return "let them eat cake"