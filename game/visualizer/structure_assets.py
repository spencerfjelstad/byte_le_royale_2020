import cocos


class PoliceLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        if self.info['player'].get('city').get('buildings').get('0').get('level') > 0:
            self.struct = self.images["police_complete"]
        else:
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


class GelatoLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        if self.info['player'].get('city').get('buildings').get('1').get('level') > 0:
            self.struct = self.images["gelato_complete"]
        else:
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


class BigCanoeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        if self.info['player'].get('city').get('buildings').get('2').get('level') > 0:
            self.struct = self.images["bigcanoe_complete"]
        else:
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


class MintLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()

        if self.info['player'].get('city').get('buildings').get('3').get('level') > 0:
            self.struct = self.images["mint_complete"]
        else:
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


class BillBoardLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets, place):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        self.place = place
        super().__init__()

        if self.info['player'].get('city').get('buildings').get('4').get('level') > 0:
            self.struct = self.images["billboard_complete"]

            # Obfuscates city name with final place
            if self.place is None:
                city_name = self.info['player']['city']['city_name']
            elif self.place is 1:
                city_name = "1st Place"
            elif self.place is 2:
                city_name = "2nd Place"
            elif self.place is 3:
                city_name = "3rd Place"

            # Display City Name, only if the billboard is built
            city_name_label = cocos.text.Label(
                city_name,
                font_name="Comic Sans",
                font_size=10,
                anchor_x="left",
                position=(self.display[0] - 100, self.display[1] - 450)
            )
            # Anchor Point of the sprite is at the center of the sprite
            # This position the sprite to the right side of the screen
            # and the sprite in the middle of the screen on the y axis
            self.sprite_width = self.struct.width
            self.sprite_height = self.struct.height

            self.struct_x = 1196
            self.struct_y = 308
            self.struct.position = (self.struct_x, self.struct_y)
            self.add(self.struct)
            self.add(city_name_label)
        else:
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


class PrintLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        self.display = display_size
        self.info = turn_info
        self.images = assets
        super().__init__()
        if self.info['player'].get('city').get('buildings').get('5').get('level') > 0:
            self.struct = self.images["3dprint_complete"]
        else:
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
