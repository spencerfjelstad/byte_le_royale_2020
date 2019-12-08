import cocos
# Display the background picture depending on the logs
class LocationLayer(cocos.layer.Layer):
    def __init__(self, turn_info, display_size, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Retrieve the player's 'location'(background) from logs
        image = str(self.info['player'].get('city').get('location'))

        # Find correlating sprite in sprite dictionary
        location = self.images[image]
        location.position = self.display[0]/2, self.display[1]/2
        self.add(location)
