import cocos


class RoadLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Depending structure draw_correct sprite
        self.city = self.images["0"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.city.width
        self.sprite_height = self.city.height

        self.city_x = int(self.display[0]-self.sprite_width/2)
        self.city_y = int(self.display[1]/2)

        self.city.position = (self.city_x, self.city_y)
        self.add(self.city)


class CityLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.city = self.images["1"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.city.width
        self.sprite_height = self.city.height

        self.city_x = int(self.display[0]-self.sprite_width/2)
        self.city_y = int(self.display[1]/2)

        self.city.position = (self.city_x, self.city_y)
        self.add(self.city)


class CityBackLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        # Depending structure draw_correct sprite
        self.city = self.images["2"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.city.width
        self.sprite_height = self.city.height

        self.city_x = int(self.display[0]-self.sprite_width/2)
        self.city_y = int(self.display[1]/2)

        self.city.position = (self.city_x, self.city_y)
        self.add(self.city)
