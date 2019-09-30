import cocos


class TimeLayer(cocos.layer.Layer):
    def __init__(self,display_size, text=0):
        self.turn = text
        self.display=display_size
        super().__init__()
        turn_label = cocos.text.Label(
            str(self.turn),
            font_name="Comic Sans",
            font_size=32
        )
        turn_label.position = 25, self.display[1]-50
        self.add(turn_label)
