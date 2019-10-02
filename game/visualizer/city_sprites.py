import cocos


class CityLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        self.display = display_size
        self.info = turn_info
        super().__init__()
        images = [
            "game/visualizer/assets/city_assets/city_default.png",
            "game/visualizer/assets/city_assets/city_level1.png",
            "game/visualizer/assets/city_assets/city_level2.png",
            "game/visualizer/assets/city_assets/city_level3.png"
        ]
        structure = 0
        try:
            structure = int(self.info['player'].get('city').get('structure'))
        except:
            print("NO! >:(")

        if structure > 150:
            self.city = cocos.sprite.Sprite(images[3])
        elif structure > 100:
            self.city = cocos.sprite.Sprite(images[2])
        elif structure > 50:
            self.city = cocos.sprite.Sprite(images[1])
        else:
            self.city = cocos.sprite.Sprite(images[0])

        self.city.position = self.display[0]-804/2, self.display[1]-498/2
        self.add(self.city)
