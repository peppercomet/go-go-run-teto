from player import Player
import pygame

class GameLogic:
    def __init__(self):
        self.player = Player()
        self.score = 0
        self.lives = 3

    def update(self):
        """Update the game state."""
        # Handle player input
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def is_game_over(self):
        """Check if the game is over."""
        return self.lives <= 0