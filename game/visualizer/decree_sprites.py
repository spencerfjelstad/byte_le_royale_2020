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
        current_turn = self.parser.get_turn(self.turn)
        disaster = -1

        # Choose image for decree based on the turn info and add it to the layer
        decree = str(info['player'].get('action').get('decree'))
        spr = self.images[decree]
        spr.position = 50, self.display[1]-50
        self.add(spr)

        success_label = cocos.text.Label("Protected!",font_name='Comic Sans',font_size=16,anchor_x='center',position=(50,self.display[1]-100))

        if len(current_turn['events']) > 0:
            if current_turn['events'][0].get('event_type') == 3:
                disaster = current_turn['events'][0].get('disaster').get('disaster_type')
        if int(decree) == disaster:
            self.add(success_label)
