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

size = DISPLAY_SIZE
log_parser = None
turn = 1


def start(gamma, fullscreen=False, endgame=True):
    global log_parser
    global turn

    log_parser = GameLogParser("logs/")

    # initialize cocos
    director.init(width=size[0], height=size[1], caption="Byte-le Royale: Disaster Dispatcher", fullscreen=fullscreen)

    # Get turn info from logs, if None go to end scene
    turn_info = log_parser.get_turn(turn)
    if turn_info is None:
        print("start")
        end = EndLayer(size)
        end_scene = cocos.scene.Scene().add(end)
        director.replace(end_scene)
    else:
        # Initialize clock layer and add an interval
        clock = TimeLayer(size, turn_info, turn)
        clock.schedule_interval(callback=timer, interval=0)

        first_scene = create_scene(turn_info)
        first_scene.add(clock)

        director.run(first_scene)


def timer(interval):
    global turn
    turn += 1
    director.scene_stack.clear()

    turn_info=log_parser.get_turn(turn)
    if turn_info is None:
        print("timer")
        end = EndLayer(size)
        end_scene = cocos.scene.Scene().add(end)
        director.replace(end_scene)
    else:
        clock = TimeLayer(size, turn_info, turn)
        clock.schedule_interval(callback=timer, interval=0.1)

        current_scene = create_scene(turn_info)
        current_scene.add(clock)

        director.replace(current_scene)


def create_scene(info):
    # Generate layers
    health_layer = HealthBar(size, info)
    location_layer = LocationLayer(size, 'plains')
    city_layer = CityLayer(size, info)

    # Add layers to
    scene = cocos.scene.Scene()
    scene.add(location_layer, 0)
    scene.add(city_layer, 1)
    scene.add(health_layer, 1)

    return scene
