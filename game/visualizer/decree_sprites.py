import cocos


class DecreeLayer(cocos.layer.Layer):
    def __init__(self, turn_info, display_size,assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Choose image for decree based on the turn info and add it to the layer
        image = str(self.info['player'].get('action').get('decree'))
        spr = self.images[image]
        spr.position = 50, self.display[1]-50
        self.add(spr)