from pygame.math import Vector2
import pathlib

# General
TOOLS = ['hoe', 'axe', 'water'] # All the tools available in the game
SEEDS = ['corn', 'tomato'] # All the seeds available in the game
ITEMS = ['corn_seed', 'tomato_seed', 'corn', 'tomato', 'hoe', 'axe', 'watering_can'] # All items in the game

# Screen
SCREEN_WIDTH = 1366#800
SCREEN_HEIGHT = 768#600
SCREEN_CAPTION = 'PYDEW VALLEY'
TILE_SIZE = 64

# Path
PARENT_PATH = pathlib.Path(__file__).parent.parent.resolve()

# Player Attributes
PLAYER_SPEED = 200
ANIMATE_PLAYER_SPEED = 4

# Paths
MAP1    = "data/map1.tmx"
MAP2    = "data/map2.tmx"

GROUND1 = 'graphics/world/ground1.png'
GROUND2 = 'graphics/world/ground2.png'

WATER   = "graphics/water"

# Overlay positions

OVERLAY_POSITIONS = {
    'tool': (40, SCREEN_HEIGHT - 15),
    'seed': (96, SCREEN_HEIGHT - 5)
}

PLAYER_TOOL_OFFSET = {
    'left': Vector2(-50, 40),
    'right': Vector2(50, 40),
    'up': Vector2(0, -10),
    'down': Vector2(0, 50),
}

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'house roof': 10,
    'rain drops': 11
}

APPLE_POS = {
    'Small': [(18, 17), (30, 37), (12, 50), (30,45), (20,30), (30,10)],
    'Large': [(30,24), (60,65), (50,50), (16,40), (45,50), (42,70)]
}

# Plants
PLANT_GROW_SPEED = {
    'corn': 1,
    'tomato': 0.7,
    'wheat': 1,
    'carrot': 1
}

PLANT_Y_OFFSET = {
    'corn': -6,
    'tomato': -8,
    'wheat': -16,
    'carrot': -8
}

# Tree
TREE_MAX_HEALTH = {"Large": 5, "Small": 3}
TREE_REVIVE_TIME = 1 # in days

# House
HOUSE_ROOF_ALPHA = 120

# Daytime and Weather
DAYTIME_SPEED = 1.5 # The speed at which the day starts darkening
DAY_NIGHT_DURATION = 40000 # In Milliseconds
RAIN_PROBABILITY = 3 # 30% chance of precipitation

# Fonts Setup
FONT_SIZE = 30
FONT_PATH = "fonts/LycheeSoda.ttf" # Place this path after the Current Working Directory 

# Shop Attributes
MENU_WIDTH = 400
MENU_SPACE = 10
MENU_PADDING = 8
SHOP_OPTIONS = ['wood', 'apple', 'corn_seed', 'tomato_seed', 'corn', 'tomato']

SALE_PRICES = {
    'wood': 4,
    'apple': 4,
    'corn': 4,
    'tomato': 4,
    'corn_seed': 4,
    'tomato_seed': 4
}

PURCHASE_PRICES = {
    'wood': 4,
    'apple': 4,
    'corn': 4,
    'tomato': 4,
    'corn_seed': 4,
    'tomato_seed': 4
}

# SOUNDS

AXE_SOUND_PATH   = "audio/axe.wav"
AXE_SOUND_VOLUME = 0.8 # 80% of the actual file volume

SUCCESS_SOUND_PATH   = "audio/success.wav"
SUCCESS_SOUND_VOLUME = 0.1

HOE_SOUND_PATH   = "audio/hoe.wav"
HOE_SOUND_VOLUME = 0.2

WATERING_SOUND_PATH   = "audio/watering.wav"
WATERING_SOUND_VOLUME = 0.3

PLANTING_SOUND_PATH   = "audio/planting.wav"
PLANTING_SOUND_VOLUME = 0.1

BG_MUSIC_SOUND_PATH   = "audio/bg1_music.wav"
BG_MUSIC_SOUND_VOLUME = 0.6