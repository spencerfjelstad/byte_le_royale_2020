import cocos


class SensorLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        for key, value in self.info["player"]["city"]["sensors"].items():
            sensor = self.images[key][str(value["level"])]
            key = int(key)
            if key == 0:
                sensor.position = 100*(int(key)+1), self.display[1] / 2
            elif key == 1:
                sensor.position = 100 * (int(key) + 1), self.display[1] / 3
            elif key == 2:
                sensor.position = 100 * (int(key) + 1), self.display[1] / 4
            elif key == 3:
                sensor.position = 100 * (int(key) + 1), self.display[1] / 5
            elif key == 4:
                sensor.position = 100 * (int(key) + 1), self.display[1] / 6
            elif key == 5:
                sensor.position = 100 * (int(key) + 1), self.display[1] / 7
            self.add(sensor)