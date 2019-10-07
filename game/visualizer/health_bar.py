import cocos


class HealthBar(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        self.display = display_size
        self.info = turn_info
        super().__init__()
        x= 200
        p_y= 100
        s_y= 70

        population = int(self.info['player'].get('city').get('population'))
        structure = int(self.info['player'].get('city').get('structure'))

        pop_label = cocos.text.Label('Population: ', font_name='Comic Sans', font_size=25,
                                     anchor_x='right', anchor_y='center')
        pop_label.position = x, p_y

        struct_label = cocos.text.Label('Structure: ', font_name='Comic Sans', font_size=25,
                                        anchor_x='right', anchor_y='center')
        struct_label.position = x, s_y

        self.add(pop_label)
        self.add(struct_label)

        pop_bar = cocos.draw.Line(start=(x+20,p_y), end=(x+20+population*4, p_y), color=(0,0,255,255), stroke_width=25)
        struct_bar = cocos.draw.Line(start=(x+20,s_y), end=(x+20+structure*4, s_y), color=(255,0,0,255), stroke_width=25)

        self.add(struct_bar)
        self.add(pop_bar)