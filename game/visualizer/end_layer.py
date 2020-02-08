import cocos
import json

from game.visualizer.graphs import *
from game.config import RESULTS_FILE


class EndLayer(cocos.layer.Layer):
    def __init__(self, display_size, parser):
        self.display = display_size
        super().__init__()
        label = cocos.text.Label(
            "Game Over",
            font_size=64,
            color=(255, 0, 0, 255),
            anchor_x='center',
            anchor_y='center'

        )
        label.position = self.display[0] / 2, self.display[1] / 2 + 300
        self.add(label)

        # Fun stats
        results = dict()
        with open(RESULTS_FILE, 'r') as f:
            results = json.load(f)
        stats = results['Statistics']

        dis_def_percent = f'{stats["disasters_correctly_protected"] / stats["total_disasters"]:.2%}'
        dis_def_label = cocos.text.Label(
            f'Disasters Defended: {stats["disasters_correctly_protected"]}/{stats["total_disasters"]}, {dis_def_percent}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='left',
            anchor_y='center'
        )
        dis_def_label.position = 50, self.display[1] / 2 + 300
        self.add(dis_def_label)

        tot_pop_dam_label = cocos.text.Label(
            f'Total Population Lost: {stats["total_population_damage"]}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='left',
            anchor_y='center'
        )
        tot_pop_dam_label.position = 50, self.display[1] / 2 + 280
        self.add(tot_pop_dam_label)

        tot_str_dam_label = cocos.text.Label(
            f'Total Structure Damaged: {stats["total_structure_damage"]}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='left',
            anchor_y='center'
        )
        tot_str_dam_label.position = 50, self.display[1] / 2 + 260
        self.add(tot_str_dam_label)

        avg_pop = f'{stats["total_population_ever"] / results["Score"]:.2f}'
        avg_pop_label = cocos.text.Label(
            f'Average Population: {avg_pop}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='right',
            anchor_y='center'
        )
        avg_pop_label.position = self.display[0] - 50, self.display[1] / 2 + 300
        self.add(avg_pop_label)

        avg_str = f'{stats["total_structure_ever"] / results["Score"]:.2f}'
        avg_str_label = cocos.text.Label(
            f'Average Structure: {avg_str}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='right',
            anchor_y='center'
        )
        avg_str_label.position = self.display[0] - 50, self.display[1] / 2 + 280
        self.add(avg_str_label)

        final_score_label = cocos.text.Label(
            f'Total Turns Survived: {results["Score"]}',
            font_size=16,
            color=(240, 240, 255, 255),
            anchor_x='right',
            anchor_y='center'
        )
        final_score_label.position = self.display[0]-50, self.display[1] / 2 + 260
        self.add(final_score_label)

        # Line graph
        # self.add(LineGraph([6,48,367], 200,100, parser))
        self.add(LineGraph(parser, self.display[0]-100, self.display[1]-100-100, 50, 50))
