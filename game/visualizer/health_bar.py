import cocos


class HealthBar(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        self.display = display_size
        self.info = turn_info
        super().__init__()
        x= 116
        p_y= 47
        s_y= 18

        population = int(self.info['player'].get('city').get('population'))
        structure = int(self.info['player'].get('city').get('structure'))

        pop_label = cocos.text.Label('Population: ', font_name='Comic Sans', font_size=15,
                                     anchor_x='right', anchor_y='center')
        pop_label.position = x, p_y

        struct_label = cocos.text.Label('Structure: ', font_name='Comic Sans', font_size=15,
                                        anchor_x='right', anchor_y='center')
        struct_label.position = x, s_y

        p_start = x+20, p_y
        p_end = x+20+population, p_y
        s_start = x+20, s_y
        s_end = x+20+structure, s_y

        self.add(pop_label)
        self.add(struct_label)

        pop_bar = cocos.draw.Line(p_start, p_end, color=(0,0,255,255), stroke_width=15)
        struct_bar = cocos.draw.Line(s_start, s_end, color=(255,0,0,255), stroke_width=15)


        self.add(struct_bar)
        self.add(pop_bar)

        mark_line_x = 128

        for i in range(9):
            mark_lines = cocos.draw.Line((mark_line_x + (i*50), 10), (mark_line_x + (i*50), 58), color=(0, 0, 0, 255), stroke_width=2)
            self.add(mark_lines)
