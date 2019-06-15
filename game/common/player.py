import uuid


class Player:
    def __init__(self, code, team_name=None, city=None):
        self.id = str(uuid.uuid4())
        self.team_name = team_name
        self.code = code
        self.city = city

    def to_json(self):
        data = dict()

        data['id'] = self.id
        data['team_name'] = self.team_name
        data['city'] = self.city
        return data

    def from_json(self, data):
        self.id = data['id']
        self.team_name = data['team_name']
        self.city = data['city']
