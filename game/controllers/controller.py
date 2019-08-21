
class Controller:

    def __init__(self):
        self.debug = False
        self.controllers = None

    def import_controllers(self, controllers):
        if not isinstance(controllers, dict):
            raise Exception("Instance {} tried importing controllers not in dictionary format.".format(self))
        self.controllers = controllers
        if "destruction" in self.controllers:
            self.destruction_controller = self.controllers["destruction"]
        if "disaster" in self.controllers:
            self.disaster_controller = self.controllers["disaster"]
        if "effort" in self.controllers:
            self.effort_controller = self.controllers["effort"]
        if "sensor" in self.controllers:
            self.sensor_controller = self.controllers["sensor"]

    def log(self, message):
        if self.debug is True:
            print(message)
