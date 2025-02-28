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
PLAYER_SPEED = 5
OBJECT_SPEED = 3  
INITIAL_LIVES = 3
POINTS_PER_OBJECT = 10
BAD_OBJECT_PENALTY = 1

# Object spawn settings
OBJECT_SPAWN_DELAY = 1000  # Time (in milliseconds) between object spawns
OBJECT_WIDTH = 50
OBJECT_HEIGHT = 50

# Player settings
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2  # Center the player horizontally
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10  # Position the player near the bottom

# File paths
ASSETS_DIR = "assets"
IMAGES_DIR = f"{ASSETS_DIR}/images"
FONTS_DIR = f"{ASSETS_DIR}/fonts"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"

# Achievement storage
ACHIEVEMENTS_FILE = "achievements.txt"

# Font settings
FONT_NAME = "arial"
FONT_SIZE = 32

# Image file paths
PLAYER_IMAGE = f"{IMAGES_DIR}/player.png"
GOOD_OBJECT_IMAGE = f"{IMAGES_DIR}/good_object.png"
BAD_OBJECT_IMAGE = f"{IMAGES_DIR}/bad_object.png"
BACKGROUND_IMAGE = f"{IMAGES_DIR}/background.jpg"
