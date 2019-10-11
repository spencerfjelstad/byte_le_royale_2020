import cocos
from cocos.actions import *


class Data(cocos.layer.Layer):

    def __init__(self, x=0, y=0):
        self.length = None
        self.height = None
        super().__init__()
        self.x = x
        self.y = y
        # Data
        test_list = [68, 380, 157, 283, 411, 357, 29, 374, 470, 66, 454, 281, 485,
                     76, 486, 460, 369, 101, 285, 247, 269, 266, 11, 449, 346, 245,
                     109, 390, 268, 497, 23, 295, 155, 366, 211, 396, 195, 398, 208,
                     436, 163, 106, 466, 407, 104, 192, 85, 43, 331, 329, 328, 149,
                     111, 373, 156, 22, 386, 279, 124, 438, 337, 382, 50, 332, 442,
                     477, 77, 30, 126, 260, 118, 310, 383, 259, 484, 461, 117, 292,
                     446, 166, 253, 132, 80, 0]

        self.length = len(test_list)*5
        self.height = max(test_list)


        # Draw lines in graph
        x_origin = 0
        y_origin = 0

        for i in range(0, len(test_list)):
            value = test_list[i]
            if i != 0:
                data_line = cocos.draw.Line((x_origin, y_origin), (x + 5*i, y + value), (255, 255, 255, 255), 1)
                self.add(data_line)
            x_origin = x + 5*i
            y_origin = y + value

        print(self.x)
        print(self.y)


class LineGraph(cocos.layer.Layer):
    def __init__(self, population_list, final_width, final_height):
        super().__init__()
        self.line_graph()



    def line_graph(self, length = 500, height = 300, x = 200, y = 100, color = (255,255,255,255)):

        #Border
        horizontal_line1 = cocos.draw.Line((x,y),(x+length, y),color, 5)
        horizontal_line2 = cocos.draw.Line((x, y+height), (x + length, y+height), color, 5)
        vertical_line1 = cocos.draw.Line((x,y), (x, y+height), color, 5)
        vertical_line2 = cocos.draw.Line((x + length, y), (x + length, y + height), color, 5)

        self.add(horizontal_line1)
        self.add(horizontal_line2)
        self.add(vertical_line1)
        self.add(vertical_line2)

        #Data
        data_layer = Data(x,y)
        self.transform_anchor_x = 0
        data_layer.transform_anchor_x = 0
        #data_layer.transform_anchor_y = 0
        data_layer.scale_x = float(length/data_layer.length)
        print(float(length/data_layer.length))
        #data_layer.scale_y = float(height/data_layer.height)
        print(float(height/data_layer.height))

        data_layer.position = (0,0)

        self.add(data_layer)

        #Ticks
        for i in range (0,9):
            #x-axis ticks
            x_tick = cocos.draw.Line((x + (length * (i+1) / 10), y),(x + (length * (i+1) / 10), y + 10),color, stroke_width = 2 )
            self.add(x_tick)

            #y-axis ticks
            y_tick = cocos.draw.Line((x, y + (height * (i + 1) / 10)), (x + 10 , y + (height * (i + 1) / 10)),color, stroke_width=2)
            self.add(y_tick)


    # #For now, here's how to draw a basic graph with random points
    # #Game results, gotten from logs
    # max_population = max(population_list)
    # max_turns = len(population_list)
    #
    # #surface to be returned
    # data_surf = pygame.Surface((max_turns,max_population))
    # surf = pygame.Surface((final_width + 4, final_height + 4))
    #
    # #Border
    # #Variables and rectangle specifications based on population and turns. To be scaled down to length and width
    # x_coord = 0
    # y_coord = 0
    # height = max_population + 5
    # width = max_turns
    #
    # data_surf.fill(pygame.Color(0, 255, 255))
    #
    # #Draw lines in graph
    # x_origin = x_coord
    # y_origin = y_coord + height
    # #Test values for y value
    # #values = [50,67,10,100,79,56,24,79,35,78,36,35,78,17,96,46,86,23,67,56]
    # for i in range(0,max_turns):
    #     population = population_list.pop(0)
    #     if(i != 0):
    #         pygame.draw.line(data_surf, pygame.Color(0,0,0), (x_origin,y_origin),(x_coord + i, y_coord + height - population))
    #     x_origin = x_coord + i
    #     y_origin = y_coord + height - population
    #
    # data_surf = pygame.transform.scale(data_surf,(final_width,final_height))
    #
    # border_width = final_width + 4
    # border_height = final_height + 4
    #
    # border = pygame.Rect(x_coord, y_coord, border_width, border_height)
    # #Inner border
    # #inner_border = pygame.Rect(x_coord + 2, y_coord + 2, width - 4, height - 4)
    # # Draw rectangles
    # pygame.draw.rect(surf, pygame.Color(0, 0, 0), border)
    # #Inner border
    # surf.blit(data_surf, (2,2))
    # #pygame.draw.rect(data_surf, pygame.Color(0, 255, 255), inner_border)
    #
    # # Ticks
    # # Calculating values at each tick for x and y
    # # Note: Only works if length is divisible by max population
    #
    # # Num of ticks to be a constant 10, the turn and pop values divided to fit
    # for i in range(0, 9):
    #     # x-axis ticks
    #     pygame.draw.line(surf, pygame.Color(0, 0, 0), (x_coord + (border_width * (i + 1) / 10), y_coord + border_height),
    #                      (x_coord + (border_width * (i + 1) / 10), y_coord + border_height - 4))
    #     # y-axis ticks
    #     pygame.draw.line(surf, pygame.Color(0, 0, 0), (x_coord, y_coord + (border_height * (i + 1) / 10)),
    #                      (x_coord + 4, y_coord + (border_height * (i + 1) / 10)))
    #
    # return surf
    # #surf.draw.rect

