import cocos
from cocos.director import director
import pyglet
import sys

from game.config import *
from game.visualizer.game_log_parser import GameLogParser
from game.visualizer.graphs import *
from game.visualizer.city_sprites import *
from game.visualizer.location_sprites import *
from game.visualizer.global_stats import GlobalStats
from game.visualizer.health_bar import *
from game.visualizer.input_layer import *
from game.visualizer.time_layer import *
from game.visualizer.end_layer import *
from game.visualizer.forecast_sprite import *
from game.visualizer.decree_sprites import *
from game.visualizer.disaster_layer import *
from game.visualizer.worker_sprites import *
from game.visualizer.load import *
from game.visualizer.sensor_sprites import *
from game.visualizer.structure_assets import *

# Global variables needed for scene creation and keeping track of turns
size = DISPLAY_SIZE
log_parser = None
end_boolean = True
assets = {}
global_stats = GlobalStats()


# Function called by main that displays first scene and initializes everything
def start(gamma, fullscreen=False, endgame=True):
    global log_parser
    global end_boolean
    end_boolean = endgame

    log_parser = GameLogParser("logs/")
    if len(log_parser.turns) < 1:
        print("Your code is broken and no turns were processed. Try again later.")
        sys.exit()

    # Initialize cocos
    director.init(width=size[0], height=size[1], caption="Byte-le Royale: Disaster Dispatcher", fullscreen=fullscreen)

    load(assets)

    # Get turn info from logs, if None go to end scene
    # on the end scene the end_boolean is checked, and if False, the visualizer will close after 4 seconds
    turn_info = log_parser.get_turn(global_stats.turn_num)
    if turn_info is None:
        end_layer = EndLayer(size, log_parser)
        end_scene = cocos.scene.Scene().add(end_layer)
        director.replace(end_scene)
        if not end_boolean:
            end_scene.schedule_interval(exit, 4)
    else:
        # Initialize clock layer and add an interval
        clock = TimeLayer(size, turn_info, global_stats.turn_num)
        clock.schedule_interval(callback=timer, interval=0)

        first_scene = create_scene(turn_info, log_parser)
        first_scene.add(clock,100)
        director.run(first_scene)


def timer(interval):

    director.scene_stack.clear()

    # Get turn info from logs, if None go to end scene
    # on the end scene the end_boolean is checked, and if False, the visualizer will close after 4 seconds
    turn_info=log_parser.get_turn(global_stats.turn_num)
    if turn_info is None:
        end_layer = EndLayer(size,log_parser)
        end_scene = cocos.scene.Scene().add(end_layer)
        director.replace(end_scene)
        if not end_boolean:
            end_scene.schedule_interval(exit, 10)
    else:
        # If a disaster happens, slow down the interval rate
        intval = global_stats.base_turn_time * global_stats.turn_speed
        for key, item in (turn_info['rates'].items()):
            if item == 0:
                intval = global_stats.disaster_turn_time * global_stats.turn_speed

        clock = TimeLayer(size, turn_info, global_stats.turn_num)
        clock.schedule_interval(callback=timer, interval=intval)
        current_scene = create_scene(turn_info, log_parser)
        current_scene.add(clock, 100)

        director.replace(current_scene)
        global_stats.turn_num += 1


# Function that generates base scene layer for the given turn
def create_scene(info, parser):
    # Generate layers
    health_layer = HealthBar(size, info)
    location_layer = LocationLayer(info, size, assets['location'])
    city_road_layer = RoadLayer(size, info, assets['city'])
    city_layer = CityLayer(size, info, assets['city'])
    city_back_layer = CityBackLayer(size, info, assets['city'])
    forecast_layer = ForecastLayer(global_stats.turn_num, size, parser, assets['forecast'])
    decree_layer = DecreeLayer(global_stats.turn_num, size, parser, assets['decree'])
    decree_hold_layer = DecreeHolderLayer(assets['decree'])
    worker_layer = WorkerLayer(size, assets['worker'])
    input_layer = InputLayer()

    # Side structures
    print_layer = PrintLayer(size, info, assets['struct'])
    bigcanoe_layer = BigCanoeLayer(size, info, assets['struct'])
    billboard_layer = BillBoardLayer(size, info, assets['struct'])
    gelato_layer = GelatoLayer(size, info, assets['struct'])
    mint_layer = MintLayer(size, info, assets['struct'])
    police_layer = PoliceLayer(size, info, assets['struct'])

    # Disasters
    fire_layer = FireLayer(size, info, assets['disaster'])
    tornado_layer = TornadoLayer(size, info, assets['disaster'])
    blizzard_layer = BlizzardLayer(size, info, assets['disaster'])
    earthquake_layer = EarthquakeLayer(size, info, assets['disaster'])
    monster_layer = MonsterLayer(size, info, assets['disaster'])
    ufo_layer = UFOLayer(size, info, assets['disaster'])

    front_sensor_layer = FrontSensorLayer(size, info, assets['sensor'])
    back_sensor_layer = BackSensorLayer(size, info, assets['sensor'])

    # Add layers to
    scene = cocos.scene.Scene()
    scene.add(location_layer, 0)
    scene.add(city_layer, 18)
    scene.add(city_back_layer, 15)
    scene.add(city_road_layer, 10)
    scene.add(worker_layer, 26)
    scene.add(front_sensor_layer, 18)
    scene.add(back_sensor_layer, 15)

    # Side Structures
    scene.add(print_layer, 19)
    scene.add(bigcanoe_layer, 19)
    scene.add(billboard_layer, 19)
    scene.add(gelato_layer, 19)
    scene.add(mint_layer, 19)
    scene.add(police_layer, 19)

    # Disasters
    scene.add(fire_layer, 20)
    scene.add(tornado_layer, 27)
    scene.add(blizzard_layer, 20)
    scene.add(earthquake_layer, 20)
    scene.add(monster_layer, 16)
    scene.add(ufo_layer, 20)

    scene.add(health_layer, 100)
    scene.add(forecast_layer, 100)
    scene.add(decree_layer, 100)
    scene.add(decree_hold_layer, 99)
    scene.add(input_layer, 100)

    return scene


# Create exit method for use with schedule_interval() such that nothing will print when used together
def exit(interval):
    sys.exit()
