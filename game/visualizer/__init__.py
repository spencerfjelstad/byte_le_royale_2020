import cocos
from cocos.director import director
import pyglet

from game.config import *
from game.visualizer.game_log_parser import GameLogParser
from game.visualizer.graphs import *
from game.visualizer.city_sprites import *
from game.visualizer.location_sprites import *
from game.visualizer.health_bar import *
from game.visualizer.time_layer import *
from game.visualizer.end_layer import *
from game.visualizer.forecast_sprite import *
from game.visualizer.decree_sprites import *

size = DISPLAY_SIZE
log_parser = None
turn = 1


def start(gamma, fullscreen=False):
    global log_parser
    global turn

    log_parser = GameLogParser("logs/")

    # initialize cocos
    director.init(width=size[0], height=size[1], caption="Byte-le Royale: Disaster Dispatcher", fullscreen=fullscreen)

    # Get turn info from logs, if None go to end scene
    turn_info = log_parser.get_turn(turn)
    if turn_info is None:
        end = EndLayer(size)
        end_scene = cocos.scene.Scene().add(end)
        director.replace(end_scene)
    else:
        # Initialize clock layer and add an interval
        clock = TimeLayer(size, turn_info, turn)
        clock.schedule_interval(callback=timer, interval=0)

        first_scene = create_scene(turn_info, log_parser)
        first_scene.add(clock)
        director.run(first_scene)


def timer(interval):
    global turn

    director.scene_stack.clear()

    turn_info=log_parser.get_turn(turn)
    if turn_info is None:
        end = EndLayer(size)
        end_scene = cocos.scene.Scene().add(end)
        director.replace(end_scene)
    else:
        clock = TimeLayer(size, turn_info, turn)
        clock.schedule_interval(callback=timer, interval=.25)

        current_scene = create_scene(turn_info, log_parser)
        current_scene.add(clock)

        director.replace(current_scene)
        turn+=1


def create_scene(info, parser):
    # Generate layers
    health_layer = HealthBar(size, info)
    location_layer = LocationLayer(size, 'plains')
    city_layer = CityLayer(size, info)
    forecast_layer = ForecastLayer(turn, size, parser)
    decree_layer = DecreeLayer(info, size)

    # Add layers to
    scene = cocos.scene.Scene()
    scene.add(location_layer, 0)
    scene.add(city_layer, 1)
    scene.add(health_layer, 1)
    scene.add(forecast_layer, 1)
    scene.add(decree_layer, 1)

    return scene
