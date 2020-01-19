import cocos


class PrintLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["3dprint"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 130
        self.struct_y = 208
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)


class BigCanoeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["bigcanoe"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 732
        self.struct_y = 324
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)


class BillBoardLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["billboard"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 1196
        self.struct_y = 308
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)


class GelatoLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["gelato"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 540
        self.struct_y = 172
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)


class MintLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["mint"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 436
        self.struct_y = 188
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)


class PoliceLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        self.struct = self.images["police"]

        # Anchor Point of the sprite is at the center of the sprite
        # This position the sprite to the right side of the screen
        # and the sprite in the middle of the screen on the y axis
        self.sprite_width = self.struct.width
        self.sprite_height = self.struct.height

        self.struct_x = 300
        self.struct_y = 196
        self.struct.position = (self.struct_x, self.struct_y)
        self.add(self.struct)
