import os

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frame rate
FPS = 60

# Colors (RGB values)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game settings
PLAYER_SPEED = 9
OBJECT_SPEED = 5
INITIAL_LIVES = 3
POINTS_PER_OBJECT = 10
BAD_OBJECT_PENALTY = 1

# Object spawn settings
OBJECT_SPAWN_DELAY = 1000  # Time between object spawns
OBJECT_WIDTH = 100
OBJECT_HEIGHT = 100

# Player settings
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120
PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2  # Center the player horizontally
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10  # Position the player near the bottom

# Hitbox settings (smaller than the actual image size)
PLAYER_HITBOX_WIDTH = 72  
PLAYER_HITBOX_HEIGHT = 80  
OBJECT_HITBOX_WIDTH = 50 
OBJECT_HITBOX_HEIGHT = 50

# File paths
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

# Achievement storage
ACHIEVEMENTS_FILE = os.path.join(os.path.dirname(__file__), "achievements.txt")

# Font settings
FONT_NAME = os.path.join(FONTS_DIR, "PokemonSolidNormal-xyWR.ttf")
FONT_SIZE = 28

# Image file paths
PLAYER_IMAGE = os.path.join(IMAGES_DIR, "player.png")
GOOD_OBJECT_IMAGE = os.path.join(IMAGES_DIR, "good_object.png")
BAD_OBJECT_IMAGE = os.path.join(IMAGES_DIR, "bad_object.png")
BACKGROUND_IMAGE = os.path.join(IMAGES_DIR, "background.jpg")
