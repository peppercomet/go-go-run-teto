import os

# Neon colors
NEON_RED = (255, 0, 0)  
NEON_GREEN = (0, 255, 0)

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
BAD_OBJECT_SPEED = 9
INITIAL_LIVES = 3
POINTS_PER_OBJECT = 10
BAD_OBJECT_PENALTY = 1

# Object spawn settings
OBJECT_SPAWN_DELAY = 1000
OBJECT_WIDTH = 100
OBJECT_HEIGHT = 100

# Player settings
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120
PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2  # Center the player horizontally
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10  # Position the player near the bottom

# Hitbox settings
PLAYER_HITBOX_WIDTH = 72  
PLAYER_HITBOX_HEIGHT = 80  
OBJECT_HITBOX_WIDTH = 50 
OBJECT_HITBOX_HEIGHT = 50

# Base directories
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")

# File paths
SOUNDTRACK_FILE = os.path.join(MUSIC_DIR, "chipi-chipi-chapa-chapa.mp3")

# Font settings
FONT_NAME = os.path.join(FONTS_DIR, "PokemonSolidNormal-xyWR.ttf")
FONT_SIZE = 28

# Image file paths
PLAYER_IMAGE = os.path.join(IMAGES_DIR, "player.png")
GOOD_OBJECT_IMAGE = os.path.join(IMAGES_DIR, "good_object.png")
BAD_OBJECT_IMAGE = os.path.join(IMAGES_DIR, "bad_object.png")
BACKGROUND_IMAGE = os.path.join(IMAGES_DIR, "background.jpg")

# Bad object settings
BAD_OBJECT_SPAWN_PROBABILITY = 0.35
BAD_OBJECT_PENALTY = 1

# Achievement storage
ACHIEVEMENTS_FILE = os.path.join(os.path.dirname(__file__), "achievements.txt")

# Achievement definitions
ACHIEVEMENTS = {
    "bread_eater": {
        "name": "Bread Eater",
        "description": "Score your first point.",
        "condition": lambda score, objects_collected, time_survived: score >= 10
    },
    "bread_collector": {
        "name": "Bread Collector",
        "description": "Collect 50 objects.",
        "condition": lambda score, objects_collected, time_survived: objects_collected >= 50
    },
    "survivor": {
        "name": "I'm Still Standing",
        "description": "Survive for 60 seconds.",
        "condition": lambda score, objects_collected, time_survived: time_survived >= 60
    },
    "high_score": {
        "name": "High Score",
        "description": "Reach a score of 500.",
        "condition": lambda score, objects_collected, time_survived: score >= 500
    },
    "very_high_score": {
        "name": "Very High Score",
        "description": "Reach a score of 1000.",
        "condition": lambda score, objects_collected, time_survived: score >= 100
    }
    
}




