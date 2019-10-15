import cocos
from cocos.actions import *


class LineGraph(cocos.layer.Layer):
    def __init__(self, population_list, final_width, final_height, parser):
        super().__init__()
        self.line_graph(parser)



    def line_graph(self, parser, length = 500, height = 300, x = 200, y = 100, color = (255,255,255,255)):

        #Border
        horizontal_line1 = cocos.draw.Line((x,y),(x+length+10, y),color, 5)
        horizontal_line2 = cocos.draw.Line((x, y+height+10), (x + length+10, y+height+10), color, 5)
        vertical_line1 = cocos.draw.Line((x,y), (x, y+height+10), color, 5)
        vertical_line2 = cocos.draw.Line((x + length+10, y), (x + length+10, y + height+10), color, 5)

        #Border
        self.add(horizontal_line1)
        self.add(horizontal_line2)
        self.add(vertical_line1)
        self.add(vertical_line2)

        #Data
        data_layer = Data(parser,x/2,y/2)
        data_layer.transform_anchor_x = x/2
        data_layer.transform_anchor_y = y/2
        data_layer.scale_x = float(length/data_layer.length)
        data_layer.scale_y = float(height/data_layer.height)

        self.add(data_layer)

        #Ticks
        for i in range (0,9):
            #x-axis ticks
            x_tick = cocos.draw.Line((x + (length * (i+1) / 10), y),(x + (length * (i+1) / 10), y + 10),color, stroke_width = 2 )
            self.add(x_tick)

            #y-axis ticks
            y_tick = cocos.draw.Line((x, y + (height * (i + 1) / 10)), (x + 10 , y + (height * (i + 1) / 10)),color, stroke_width=2)
            self.add(y_tick)


class Data(cocos.layer.Layer):
    def __init__(self, parser, x=0, y=0):
        self.length = None
        self.height = None
        super().__init__()
        self.x = x
        self.y = y
        self.parser = parser
        population_list = []

        # Data
        for i in self.parser.turns:
            population_list.append(i['player']['city']['population'])

        self.length = len(population_list)*3
        self.height = max(population_list)


        # Draw lines in graph
        x_origin = 0
        y_origin = 0

        for i in range(0, len(population_list)):
            value = population_list[i]
            if i != 0:
                data_line = cocos.draw.Line((x_origin, y_origin), (x + 3*i, y + value), (255, 255, 255, 255), 1)
                self.add(data_line)
            x_origin = x + 3*i
            y_origin = y + value

