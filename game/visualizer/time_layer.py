import cocos


class TimeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, text=0):
        self.turn = text
        self.display = display_size
        self.info = turn_info
        super().__init__()
        turn_label = cocos.text.Label(
            str(self.turn),
            font_name="Comic Sans",
            font_size=32
        )
        turn_label.position = 25, self.display[1]-50
        self.add(turn_label)

        # Display actual rates
        n = 0
        for key, item in self.info['rates'].items():
            n+=1
            text = f'{key}: {item}'
            label = cocos.text.Label(
                text,
                font_name="Comic Sans",
                font_size=15
            )
            label.position = 30, self.display[1]-50-30*n
            self.add(label)

        # Display city sensor
        n = 0
        for sensor in self.info['player']['city']['sensors'].values():
            n += 1
            text = f'{sensor["sensor_type"]}: {sensor["sensor_results"]}'
            label = cocos.text.Label(
                text,
                font_name="Comic Sans",
                font_size=15
            )
            label.position = 500, self.display[1]-50-30 * n
            self.add(label)
