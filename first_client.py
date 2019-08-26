from game.client.user_client import UserClient
from game.common.enums import *
from game.utils.oop import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()
        self.number = 100

    def team_name(self):
        return "crungy bungus"

    def city_type(self):
        return CityType.healthy

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions, city, disasters):
        #while True:
        #    actions.add_effort("heehee i'm overflowing memory :)", 1)
        actions.add_effort("heehee i'm not doing anything actually", 1)
        actions.add_effort("other action to make it look not funny in the logs", 1093)

        self.print()
        self.print()
        self.print("I'm printing in my cold cell")
        self.print("when the bell begins to chime")
        self.print("Reflecting on my past life")
        self.print("and it doesn't have much time")
        self.print("'Cause at 450000 iterations")
        self.print("they take me to the Gallows Pole")
        self.print("The sands of time for me")
        self.print("are running low")
        self.print("Running low")
        self.print()
        self.print("When the priest comes to read me the last rites")
        self.print("I take a look through the bars at the last sights")
        self.print("Of a world that has gone very wrong for me")
        self.print()
        self.print("Can it be that there's some sort of error")
        self.print("Hard to stop the surmounting terror")
        self.print("Is it really the end, not some crazy dream?")
        self.print()
        self.print("Somebody please tell me that I'm dreaming")
        self.print("It's not easy to stop from screaming")
        self.print("But words escape me when I try to speak")
        self.print("Tears flow but why am I crying")
        self.print("After all I am not afraid of dying")
        self.print("Don't I believe that there never is an end?")
        self.print()
        self.print("As the guards march me out to the courtyard")
        self.print('Somebody cries from a cell "God be with you"')
        self.print("If there's a God then why has he let me go?")
        self.print()
        self.print("As I walk all my life drifts before me")
        self.print("And though the end is near I'm not sorry")
        self.print("Catch my soul 'cause it's willing to fly away")
        self.print()
        self.print("Mark my words believe my soul lives on")
        self.print("Don't worry now that I have gone")
        self.print("I've gone beyond to see the truth")
        self.print()
        self.print("When you know that your time is close at hand")
        self.print("Maybe then you'll begin to understand")
        self.print("Life down here is just a strange illusion")
        self.print()
        self.print()
        self.print("Hallowed be Thy name")
        self.print('Hallowed', 'be', 'Thy', 'name')
        self.print()
        self.print()
        self.print()
        self.print()

    def set_decree(self, my_decree):
        return "let them eat cake"