import cocos


class TimeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, text=0):
        self.turn = text
        self.display = display_size
        self.info = turn_info
        super().__init__()

        # Display player's team name
        team_name_label = cocos.text.Label(
            self.info['player']['team_name'],
            font_name="Comic Sans",
            font_size=20,
            anchor_x="center",
            position=(self.display[0]/2, self.display[1] - 126)
        )
        self.add(team_name_label)

        # Display current turn number
        turn_label = cocos.text.Label(
            str(self.turn),
            font_name="Comic Sans",
            font_size=24,
            anchor_x="right"
        )
        turn_label.position = self.display[0], self.display[1] - 32

        # Display player's wealth/gold
        gold = self.info['player']['city']['gold']
        gold_label = cocos.text.Label(
            f"Gold: {gold}",
            font_name="Comic Sans",
            font_size=15,
            color=(255,215,0,255),
            anchor_x="right"
        )
        gold_label.position = self.display[0]-8, 32

        self.add(turn_label)
        self.add(gold_label)
