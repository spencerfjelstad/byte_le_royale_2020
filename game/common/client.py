import uuid


class PublicClient:
    def __init__(self, object_thing_that_the_player_controls):
        self.public_id = str(uuid.uuid4())
        self.object_thing_that_the_player_controls = object_thing_that_the_player_controls


class Client:
    def __init__(self, code, object_thing_that_the_player_controls):
        self.id = str(uuid.uuid4())
        self.code = code
        self.public_client = PublicClient(object_thing_that_the_player_controls)
