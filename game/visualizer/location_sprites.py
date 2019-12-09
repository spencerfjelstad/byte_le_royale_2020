import cocos


# Display the background picture depending on the logs
class LocationLayer(cocos.layer.Layer):
    def __init__(self, turn_info, display_size, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Find correlating sprite in sprite dictionary
        location = self.images["0"]
        location.position = self.display[0]/2, self.display[1]/2
        self.add(location)
