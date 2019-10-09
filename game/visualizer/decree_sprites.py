import cocos


class DecreeLayer(cocos.layer.Layer):
    def __init__(self, turn_info):
        self.info = turn_info
        super().__init__()

        text = self.info['player'].get('action').get('decree')
        label = cocos.text.Label(str(text) if text is not None else 'NO', (25, 200), font_size=32)
        self.add(label)