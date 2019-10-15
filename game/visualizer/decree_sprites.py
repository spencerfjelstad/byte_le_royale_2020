import cocos


class DecreeLayer(cocos.layer.Layer):
    def __init__(self, turn_info, display_size):
        self.display = display_size
        self.info = turn_info
        super().__init__()
        images = {
            "0":"game/visualizer/assets/decree_assets/decree_0.png",
            "1":"game/visualizer/assets/decree_assets/decree_1.png",
            "2":"game/visualizer/assets/decree_assets/decree_2.png",
            "3":"game/visualizer/assets/decree_assets/decree_3.png",
            "4":"game/visualizer/assets/decree_assets/decree_4.png",
            "5":"game/visualizer/assets/decree_assets/decree_5.png"
        }

        image = str(self.info['player'].get('action').get('decree'))
        spr = cocos.sprite.Sprite(images[image])
        spr.position = 50, self.display[1]-50
        self.add(spr)