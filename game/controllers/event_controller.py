from game.controllers.singleton_controller import SingletonController


class EventController(SingletonController):
    EVENT_REQ = {
        "type",
        "turn",
    }

    def __init__(self):
        super().__init__()
        self.debug = False
        self.events = list()  # list instead of set here, because set cannot be converted to JSON

    def add_event(self, log):
        for req in EventController.EVENT_REQ:
            if req not in log:
                print(f"attempted to log an event without requirement '{req}'.")
                return

        self.events.append(log)

    def get_events(self, key, value):
        return [event for event in self.events if key in event and event[key] == value]
