import cocos


class LocationLayer(cocos.layer.Layer):
    def __init__(self, turn_info, display_size, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        image = str(self.info['player'].get('city').get('location'))
        location = self.images[image]
        location.position = self.display[0]/2, self.display[1]/2
        self.add(location)
