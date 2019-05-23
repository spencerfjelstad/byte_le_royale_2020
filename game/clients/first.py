from game.client.user_client import UserClient
from game.utils.oop import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()
        self.number = 100

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions):
        #while True:
        #    actions.add_effort("heehee i'm overflowing memory :)", 1)
        actions.add_effort("heehee i'm not doing anything actually", 1)
