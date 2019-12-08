import cocos


class DecreeLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, log_parser, assets):
        self.turn = turn
        self.display = display_size
        self.parser = log_parser
        self.images = assets
        super().__init__()
        if self.turn > 1:
            info = self.parser.get_turn(self.turn-1)
        else:
            info = self.parser.get_turn(self.turn)
        # Choose image for decree based on the turn info and add it to the layer
        image = str(info['player'].get('action').get('decree'))
        spr = self.images[image]
        spr.position = 50, self.display[1]-50
        self.add(spr)