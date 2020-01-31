import cocos
from cocos.actions import *


class LineGraph(cocos.layer.Layer):
    is_event_handler = True

    # def __init__(self, population_list, final_width, final_height, parser):
    def __init__(self, parser, length=500, height=300, x=200, y=100, color=(255, 255, 255, 255)):
        super().__init__()

        self.graphlen = length
        self.graphheight = height
        self.graphx = x
        self.graphy = y
        self.graphc = color

        population_list = list()
        structure_list = list()
        gold_list = list()
        self.graph_dict = {
            49: {
                'points': population_list,
                'title': 'Population',
                'color': (0, 0, 255, 255),
            },
            50: {
                'points': structure_list,
                'title': 'Structure',
                'color': (255, 0, 0, 255),
            },
            51: {
                'points': gold_list,
                'title': 'Gold',
                'color': (255, 255, 0, 255),
            },
        }
        self.current_graph = 49

        # Data
        for i in parser.turns:
            population_list.append(i['player']['city']['population'])
            structure_list.append(i['player']['city']['structure'])
            gold_list.append(i['player']['city']['gold'])

        self.graph_border(self.graphlen, self.graphheight, self.graphx, self.graphy, self.graphc)
        self.line_graph(self.graphlen, self.graphheight, self.graphx, self.graphy)

    def on_key_press(self, key, modifiers):
        if key in self.graph_dict:
            self.current_graph = key

            self.remove(self.data_layer)
            self.remove(self.title)

            self.line_graph(self.graphlen, self.graphheight, self.graphx, self.graphy)

    def graph_border(self, length, height, x, y, color):
        # Border
        horizontal_line1 = cocos.draw.Line((x, y), (x + length + 10, y), color, 5)
        horizontal_line2 = cocos.draw.Line((x, y + height + 10), (x + length + 10, y + height + 10), color, 5)
        vertical_line1 = cocos.draw.Line((x, y), (x, y + height + 10), color, 5)
        vertical_line2 = cocos.draw.Line((x + length + 10, y), (x + length + 10, y + height + 10), color, 5)

        # Border
        self.add(horizontal_line1)
        self.add(horizontal_line2)
        self.add(vertical_line1)
        self.add(vertical_line2)

        # Ticks
        for i in range(0, 9):
            # x-axis ticks
            x_tick = cocos.draw.Line((x + (length * (i + 1) / 10), y), (x + (length * (i + 1) / 10), y + 10), color,
                                     stroke_width=2)
            self.add(x_tick)

            # y-axis ticks
            y_tick = cocos.draw.Line((x, y + (height * (i + 1) / 10)), (x + 10, y + (height * (i + 1) / 10)), color,
                                     stroke_width=2)
            self.add(y_tick)

    def line_graph(self, length, height, x, y):
        #Data
        self.data_layer = Data(self.graph_dict[self.current_graph]['points'], self.graph_dict[self.current_graph]['color'], x / 2, y / 2)
        self.data_layer.transform_anchor_x = x/2
        self.data_layer.transform_anchor_y = y/2
        self.data_layer.scale_x = float(length / self.data_layer.length)
        self.data_layer.scale_y = float(height / self.data_layer.height)

        self.add(self.data_layer)

        # Add graph title
        self.title = cocos.text.Label(
            self.graph_dict[self.current_graph]['title'],
            font_name="Comic Sans",
            font_size=16,
            color=self.graph_dict[self.current_graph]['color'],
            anchor_x='center',
            anchor_y='center'

        )
        self.title.position = 640, 25
        self.add(self.title)


class Data(cocos.layer.Layer):
    def __init__(self, item_list, color, x=0, y=0):
        self.length = None
        self.height = None
        super().__init__()
        self.x = x
        self.y = y

        self.length = len(item_list)*3
        self.height = max(item_list)

        x_origin = 0
        y_origin = 0

        for i in range(0, len(item_list)):
            value = item_list[i]
            if i != 0:
                data_line = cocos.draw.Line((x_origin, y_origin), (self.x + 3 * i, self.y + value), color, 1)
                self.add(data_line)
            x_origin = self.x + 3 * i
            y_origin = self.y + value
