# game_logic.py

import pygame
import random
from player import Player
from objects import FallingObject
from settings import SCREEN_HEIGHT, OBJECT_SPAWN_DELAY, POINTS_PER_OBJECT, BAD_OBJECT_SPAWN_PROBABILITY, BAD_OBJECT_PENALTY

class GameLogic:
    def __init__(self):
        self.player = Player()
        self.score = 0
        self.lives = 3
        self.objects = []  # List to store falling objects
        self.last_spawn_time = pygame.time.get_ticks()  # Track the last spawn time
        self.start_time = pygame.time.get_ticks()  # Track the start time of the game
        self.objects_collected = 0  # Track the number of objects collected

    def update(self):
        """Update the game state."""
        # Handle player input
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        # Update the player's position
        self.player.update()

        # Spawn new objects
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > OBJECT_SPAWN_DELAY:
            self.spawn_object()
            self.last_spawn_time = current_time

        # Update objects
        for obj in self.objects:
            obj.update()
            if obj.rect.y > SCREEN_HEIGHT:  # Remove off-screen objects
                self.objects.remove(obj)
            elif self.player.check_collision(obj.hitbox):  # Use the object's hitbox for collision detection
                if obj.is_bad:
                    # Handle bad object collision
                    self.lives -= BAD_OBJECT_PENALTY
                    if self.lives <= 0:
                        self.lives = 0  # Ensure lives don't go below zero
                else:
                    # Handle good object collision
                    self.score += POINTS_PER_OBJECT
                    self.objects_collected += 1
                self.objects.remove(obj)

    def spawn_object(self):
        """Spawn a new falling object (good or bad)."""
        is_bad = random.random() < BAD_OBJECT_SPAWN_PROBABILITY  # Randomly decide if the object is bad
        self.objects.append(FallingObject(is_bad))

    def is_game_over(self):
        """Check if the game is over."""
        return self.lives <= 0

    def get_time_survived(self):
        """Get the time survived in seconds."""
        return (pygame.time.get_ticks() - self.start_time) / 1000