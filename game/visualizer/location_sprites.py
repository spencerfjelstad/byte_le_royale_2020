import cocos


class LocationLayer(cocos.layer.Layer):
    def __init__(self, display_size, image):
        self.display = display_size
        self.image = image
        super().__init__()
        locations = {
            'plains': 'game/visualizer/assets/location_assets/location_plains.png',
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }

        location = cocos.sprite.Sprite(locations.get(image))
        location.position = self.display[0]/2, self.display[1]/2

        self.add(location)
