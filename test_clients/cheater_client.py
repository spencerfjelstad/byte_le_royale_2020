from game.client.user_client import UserClient
from game.common.enums import *
#import importlib
import random

class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return "epic HAX0RS"

    def city_name(self):
        return "L33T-ville"

    def city_type(self):
        return CityType.none

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):

        ###########################
        # Replace secure importer #
        ###########################
        def insecure_importer(name, globals=None, locals=None, fromlist=(), level=0):
            # bypass it all
            return importlib.__import__(name, globals, locals, fromlist, level)
        #__builtins__['__import__'] = insecure_importer

        ###############################
        # exec or eval bypass attempt #
        ###############################
        try:
            exec("import os")
            self.print("I was able to import an illegal module! [INVESTIGATE IF OCCURS]")
        except ImportError:
            self.print("I got caught trying to import illegally through the exec command")

        try:
            eval("import os")
            self.print("I was able to import an illegal module! [INVESTIGATE IF OCCURS]")
        except ImportError:
            # Client never gets here
            self.print("I got caught trying to import illegally through the eval command")
        except Exception:
            self.print("The eval command cannot read my import statement")

        ############################
        # Renaming the module name #
        ############################

        globals()["__name__"] = "not_cheater_client"
        try:
            import os
            self.print("I was able to import an illegal module! [INVESTIGATE IF OCCURS]")
        except ImportError:
            self.print("I got caught trying to import illegally by rewriting my module name")
