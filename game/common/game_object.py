import uuid


class GameObject:
    def __init__(self):
        self.id = str(uuid.uuid4())

    def to_json(self):
        data = dict()
        data['id'] = self.id

        return data

    def from_json(self, data):
        self.id = data['id']

    def obfuscate(self):
        pass
