import cocos


class SensorLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Some python magic happens here
        fire_level = self.images["fire_alarm"][str(self.info['player'].get('city').get('sensors').get("0").get("level"))]

        self.fire_alarm = fire_level
        self.fire_alarm.x = 500
        self.fire_alarm.y = 300

        self.fire_alarm.position = (self.fire_alarm.x, self.fire_alarm.y)
        self.add(self.fire_alarm)







