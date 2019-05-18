import uuid


class Player:
    def __init__(self, code, object_thing_that_the_player_controls):
        self.id = str(uuid.uuid4())
        self.code = code
        self.object_thing_that_the_player_controls = object_thing_that_the_player_controls
