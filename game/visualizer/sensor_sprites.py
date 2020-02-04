import cocos


class BackSensorLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        for key, value in self.info["player"]["city"]["sensors"].items():
            sensor = self.images[key][str(value["level"])]
            threat = self.images[key][determine_threat(value["sensor_results"])]
            key = int(key)
            if key == 0:
                sensor.position = 1228, self.display[1]-260
            elif key == 1:
                sensor.position = 996, self.display[1]-256
            elif key == 2:
                sensor.position = 748, self.display[1]-164
            elif key == 3:
                sensor.position = 220, self.display[1]-304
            threat.position = sensor.position
            self.add(sensor)
            self.add(threat)

class FrontSensorLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        for key, value in self.info["player"]["city"]["sensors"].items():
            sensor = self.images[key][str(value["level"])]
            threat = self.images[key][determine_threat(value["sensor_results"])]
            key = int(key)
            if key == 4:
                sensor.position = 532, self.display[1]-300
            elif key == 5:
                sensor.position = 44, self.display[1]-388
            threat.position = sensor.position
            self.add(sensor)
            self.add(threat)

def determine_threat(results):
    if results == 0.0:
        return "threat_3"
    elif results <= 0.25:
        return "threat_1"
    elif results <= 0.5:
        return "threat_2"
    else:
        return "threat_3"
