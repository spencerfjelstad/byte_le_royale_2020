import cocos
from cocos.actions import *
import pyglet
import os
import shutil
from zipfile import ZipFile
from PIL import Image
from io import BytesIO
import numpy as np
import random

from game.visualizer.colors import *
from game.visualizer.global_stats import GlobalStats


global_stats = GlobalStats()

# Extracts a png from a zipped file and returns it for use with cocos.
# This function is necessary for the visualizer to work on Linux.
# Call it on each individual image before passing it to cocos.sprite.Sprite
def find_image(filename):
    archive = ZipFile("launcher.pyz",'r')
    img = Image.open(BytesIO(archive.read(filename)))
    file = filename.split('/')[-1]
    if not os.path.exists('.temp'):
        os.mkdir('.temp')
    img.save(f'.temp/{file}')
    pic = pyglet.image.load(f'.temp/{file}')
    return pic


# Deletes any temporary folders and other clean-up, called at end of load function
def clean_up():
    shutil.rmtree('.temp')


# Color replacer
def replace_colors(filename, start_colors, end_colors):
    im = Image.open(filename)
    data = np.array(im)
    for i in range(len(start_colors)):
        r1,g1,b1 = start_colors[i]
        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:3][mask] = end_colors[i]
    img = Image.fromarray(data)
    if not os.path.exists('tempic'):
        os.mkdir('tempic')
    img.save("tempic/tempimage.png")
    pic = pyglet.image.load("tempic/tempimage.png")
    shutil.rmtree("tempic")
    return pic


# Populates a dictionary with all the sprites required for the visualizer
def load(temp):
    assets = temp
    plains = cocos.sprite.Sprite(find_image("game/visualizer/assets/location_assets/location_plains.png"))
    mountains = cocos.sprite.Sprite(find_image("game/visualizer/assets/location_assets/location_mountain.png"))

    # Get random location
    num = random.randint(0,1)
    if num == 0:
        location = mountains
    else:
        location = plains

    assets['location'] = {
        "0": location,
    }

    # City assets
    city_road = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_road.png"))
    city_front = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_front.png"))
    city_back = cocos.sprite.Sprite(find_image("game/visualizer/assets/city_assets/city_back.png"))
    assets['city'] = {
        "0": city_road,
        "1": city_front,
        "2": city_back
    }

    # Side Structures
    struct_3dprint_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/3dprint_sheet.png"), 1, 2)
    struct_3dprint = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_3dprint_grid[0::], 0))
    struct_3dprint_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_3dprint_grid[1::], 0))

    struct_bigcanoe_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/bigcanoe_sheet.png"), 1, 2)
    struct_bigcanoe = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_bigcanoe_grid[0::], 0))
    struct_bigcanoe_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_bigcanoe_grid[1::], 0))

    struct_billboard_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/billboard_sheet.png"), 1, 2)
    struct_billboard = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_billboard_grid[0::], 0))
    struct_billboard_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_billboard_grid[1::], 0))

    struct_gelato_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/gelato_sheet.png"), 1, 2)
    struct_gelato = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_gelato_grid[0::], 0))
    struct_gelato_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_gelato_grid[1::], 0))

    struct_mint_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/mint_sheet.png"), 1, 2)
    struct_mint = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_mint_grid[0::], 0))
    struct_mint_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_mint_grid[1::], 0))

    struct_police_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/structure_assets/police_sheet.png"), 1, 2)
    struct_police = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_police_grid[0::], 0))
    struct_police_complete = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(struct_police_grid[1 ::], 0))

    assets['struct'] = {
        "3dprint": struct_3dprint,
        "3dprint_complete": struct_3dprint_complete,
        "bigcanoe": struct_bigcanoe,
        "bigcanoe_complete": struct_bigcanoe_complete,
        "billboard": struct_billboard,
        "billboard_complete": struct_billboard_complete,
        "gelato": struct_gelato,
        "gelato_complete": struct_gelato_complete,
        "mint": struct_mint,
        "mint_complete": struct_mint_complete,
        "police": struct_police,
        "police_complete": struct_police_complete
    }

    # Disaster assets
    dis_tornado = cocos.sprite.Sprite(find_image("game/visualizer/assets/disaster_assets/tornado.png"))

    dis_blizzard_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/disaster_assets/blizzard_sheet.png"), 1, 4)
    dis_blizzard = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(dis_blizzard_grid[0::], 0.1))

    dis_earthquake_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/disaster_assets/earthquake_sheet.png"), 1, 19)
    dis_earthquake = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(dis_earthquake_grid[0::], global_stats.base_turn_time))
    dis_earthquake.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))

    dis_monster_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/disaster_assets/monster_sheet.png"), 1, 5)
    dis_monster = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(dis_monster_grid[0::], global_stats.base_turn_time))
    dis_monster.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))

    dis_ufo_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/disaster_assets/ufo_sheet.png"), 1, 19)
    dis_ufo = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(dis_ufo_grid[0::], 0.03))

    assets['disaster'] = {}
    assets['disaster']['fire'] = list()
    assets['disaster']['tornado'] = dis_tornado
    assets['disaster']['blizzard'] = dis_blizzard
    assets['disaster']['earthquake'] = dis_earthquake
    assets['disaster']['monster'] = dis_monster
    assets['disaster']['ufo'] = dis_ufo

    for i in range(20):
        dis_fire_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/disaster_assets/fire_sheet.png"), 1, 5)
        dis_fire = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(dis_fire_grid[0::], global_stats.base_turn_time))
        dis_fire.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))

        assets['disaster']['fire'].append(dis_fire)

    # Forecast assets
    assets['forecast'] = {}
    assets['forecast']['fire'] = list()
    assets['forecast']['tornado'] = list()
    assets['forecast']['tornado'] = list()
    assets['forecast']['blizzard'] = list()
    assets['forecast']['earthquake'] = list()
    assets['forecast']['monster'] = list()
    assets['forecast']['ufo'] = list()
    assets['forecast']['clear'] = list()
    assets['forecast']['clear2'] = list()
    assets['forecast']['clear3'] = list()

    for i in range(5):
        fore_fire = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_fire.png"))
        fore_tornado = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_tornado.png"))
        fore_blizzard = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_blizzard.png"))
        fore_earthquake = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_earthquake.png"))
        fore_monster = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_monster.png"))
        fore_ufo = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_ufo.png"))
        fore_clear = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_clear.png"))
        fore_clear2 = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_clear2.png"))
        fore_clear3 = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/tape_clear3.png"))
        assets['forecast']['fire'].append(fore_fire)
        assets['forecast']['tornado'].append(fore_tornado)
        assets['forecast']['blizzard'].append(fore_blizzard)
        assets['forecast']['earthquake'].append(fore_earthquake)
        assets['forecast']['monster'].append(fore_monster)
        assets['forecast']['ufo'].append(fore_ufo)
        assets['forecast']['clear'].append(fore_clear)
        assets['forecast']['clear2'].append(fore_clear2)
        assets['forecast']['clear3'].append(fore_clear3)

    fore_holder_grid = pyglet.image.ImageGrid(find_image("game/visualizer/assets/forecast_assets/forecast_hold.png"), 1, 2)
    fore_holder = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(fore_holder_grid[0::], 0.1))
    assets['forecast']['forecast_hold'] = fore_holder

    # Disaster Level Assets
    assets['disaster_level'] = {}
    assets['disaster_level']['bronze'] = list()
    assets['disaster_level']['silver'] = list()
    assets['disaster_level']['gold'] = list()
    assets['disaster_level']['uranium'] = list()

    for i in range(5):
        # Disaster Level Assets
        bronze = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/bronze.png"))
        silver = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/silver.png"))
        gold = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/gold.png"))
        uranium = cocos.sprite.Sprite(find_image("game/visualizer/assets/forecast_assets/uranium.png"))
        assets['disaster_level']['bronze'].append(bronze)
        assets['disaster_level']['silver'].append(silver)
        assets['disaster_level']['gold'].append(gold)
        assets['disaster_level']['uranium'].append(uranium)

    # Sensor assets
    assets['sensor'] = {
        "0":{},
        "1":{},
        "2":{},
        "3":{},
        "4":{},
        "5":{},
    }
    sensor_colors = {
        0 : COLOR.red,
        1 : COLOR.black,
        2 : COLOR.blue,
        3 : COLOR.brown,
        4 : COLOR.green,
        5 : COLOR.gray,
    }
    find_image("game/visualizer/assets/sensor_assets/fire_alarm.png")
    for i in range(6):
        sensor = replace_colors(".temp/fire_alarm.png",[COLOR.red],[sensor_colors[i]])
        sensor_grid = pyglet.image.ImageGrid(sensor, 1, 2)
        level_0 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], global_stats.base_turn_time))
        level_1 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], global_stats.base_turn_time))
        level_2 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], global_stats.base_turn_time))
        level_3 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], global_stats.base_turn_time))
        assets['sensor'][str(i)].update({"0": level_0})
        assets['sensor'][str(i)].update({"1": level_1})
        assets['sensor'][str(i)].update({"2": level_2})
        assets['sensor'][str(i)].update({"3": level_3})

    # Decree assets
    decree_0 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/anti_fire_dogs.png"))
    decree_1 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/paperweights.png"))
    decree_2 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/snow_shovels.png"))
    decree_3 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/rubber_boots.png"))
    decree_4 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/fishing_hook.png"))
    decree_5 = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/cheese.png"))
    decree_holder = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/decree_holder.png"))
    decree_default = cocos.sprite.Sprite(find_image("game/visualizer/assets/decree_assets/decree_default.png"))
    assets['decree'] = {
        "-1": decree_default,
        "0": decree_0,
        "1": decree_1,
        "2": decree_2,
        "3": decree_3,
        "4": decree_4,
        "5": decree_5,
        "6": decree_holder
    }

    # Worker assets
    wrkr_colors = [[255, 255, 255], [169, 169, 169], [120, 120, 120], [67, 67, 67], [88, 88, 88]]
    skin_colors = [COLOR.russet,COLOR.peru,COLOR.fawn,COLOR.apricot,COLOR.white]
    shirt_1_colors = [COLOR.red,COLOR.magenta,COLOR.blue,COLOR.cyan,COLOR.lime,COLOR.yellow,COLOR.silver]
    shirt_2_colors = [COLOR.maroon,COLOR.olive,COLOR.green,COLOR.purple,COLOR.teal,COLOR.navy]
    pants_colors = [COLOR.khaki,COLOR.denim,COLOR.denim2,COLOR.gray]
    shoe_colors = [COLOR.brown,COLOR.cocoa,COLOR.black]

    assets['worker'] = {}
    assets['worker']['normal'] = list()
    assets['worker']['hammer'] = list()
    assets['worker']['money'] = list()
    assets['worker']['pick'] = list()
    assets['worker']['phone'] = list()
    wrkr_total = 100
    find_image("game/visualizer/assets/worker.png")
    for i in range(wrkr_total):
        wrkr = replace_colors(".temp/worker.png",wrkr_colors,[random.choice(skin_colors),
                                                                               random.choice(shirt_1_colors),
                                                                               random.choice(shirt_2_colors),
                                                                               random.choice(pants_colors),
                                                                               random.choice(shoe_colors)])
        wrkr_grid = pyglet.image.ImageGrid(wrkr, 1, 48)
        if i < wrkr_total/5:
            wrkr_normal = pyglet.image.Animation.from_image_sequence(wrkr_grid[0:15:], global_stats.base_turn_time, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_normal)
            sprite.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))
            assets['worker']['normal'].append(sprite)
        elif i < wrkr_total*2/5:
            wrkr_hammer = pyglet.image.Animation.from_image_sequence(wrkr_grid[16:23:], global_stats.base_turn_time, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_hammer)
            sprite.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))
            assets['worker']['hammer'].append(sprite)
        elif i < wrkr_total*3/5:
            wrkr_money = pyglet.image.Animation.from_image_sequence(wrkr_grid[24:31:], global_stats.base_turn_time, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_money)
            sprite.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))
            assets['worker']['money'].append(sprite)
        elif i < wrkr_total*4/5:
            wrkr_pick = pyglet.image.Animation.from_image_sequence(wrkr_grid[32:39:], global_stats.base_turn_time, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_pick)
            sprite.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))
            assets['worker']['pick'].append(sprite)
        else:
            wrkr_phone = pyglet.image.Animation.from_image_sequence(wrkr_grid[40:47:], global_stats.base_turn_time, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_phone)
            sprite.do(Repeat(CallFuncS(match_speed, global_stats.base_turn_time)))
            assets['worker']['phone'].append(sprite)
    clean_up()
    return assets


# Animations need to repeat this action in order for their frame speed to match the current speed
def match_speed(target, base_speed):
    # From the target's animation, get the current active frame and set its duration
    target._animation.frames[target._frame_index].duration = base_speed * global_stats.turn_speed

