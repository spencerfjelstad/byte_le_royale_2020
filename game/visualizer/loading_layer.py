import cocos

from game.visualizer.load import load, find_image


class LoadingLayer(cocos.layer.Layer):
    def __init__(self, assets, post_method):
        super().__init__()

        self.assets = assets
        self.post_method = post_method

        loading_image = cocos.sprite.Sprite(
            find_image('game/visualizer/assets/city_assets/loading_screen.png'),
            (640, 360),
        )
        self.add(loading_image)

        self.loading_order = {
            1: 'Loading city assets',
            2: 'Loading side structures',
            3: 'Creating disasters',
            4: 'Initializing forecasts',
            5: 'Constructing sensors',
            6: 'Writing decrees',
            7: 'Importing workers',
            8: 'Cleaning up'
        }

        self.label = cocos.text.Label(
            '',
            font_name='Arial',
            font_size=16,
            color=(0, 125, 0, 255),
            anchor_x='center',
            anchor_y='center'

        )
        self.label.position = 640, 50
        self.add(self.label)

        self.bar = cocos.draw.Line(
            (540, 30),
            (540, 30),
            color=(0, 125, 0, 255),
            stroke_width=16
        )
        self.add(self.bar)

        self.current_key = 0
        self.schedule_interval(callback=self.load_assets, interval=0.5)

    def load_assets(self, interval):
        self.current_key += 1

        if self.current_key in self.loading_order:
            item = self.loading_order[self.current_key]

            self.label.element.text = item
            self.bar.end = (540 + (200 * self.current_key / len(self.loading_order)), 30)

            load(self.assets, self.current_key)
        else:
            self.post_method()
