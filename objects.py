# objects.py

import pygame
import random
from settings import SCREEN_WIDTH, OBJECT_SPEED, BAD_OBJECT_SPEED, OBJECT_WIDTH, OBJECT_HEIGHT, GOOD_OBJECT_IMAGE, BAD_OBJECT_IMAGE, OBJECT_HITBOX_WIDTH, OBJECT_HITBOX_HEIGHT

class FallingObject:
    def __init__(self, is_bad=False):
        # Load the appropriate image based on whether the object is bad
        self.is_bad = is_bad
        self.image = pygame.image.load(BAD_OBJECT_IMAGE if is_bad else GOOD_OBJECT_IMAGE)
        self.image = pygame.transform.scale(self.image, (OBJECT_WIDTH, OBJECT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect.y = -OBJECT_HEIGHT  # Start above the screen
        self.speed = BAD_OBJECT_SPEED if is_bad else OBJECT_SPEED  # Use faster speed for bad objects

        # Define the hitbox (smaller than the image rectangle)
        self.hitbox = pygame.Rect(0, 0, OBJECT_HITBOX_WIDTH, OBJECT_HITBOX_HEIGHT)
        self.update_hitbox()  # Position the hitbox correctly

    def update_hitbox(self):
        """Update the hitbox position to align with the object's position."""
        self.hitbox.center = self.rect.center

    def update(self):
        """Move the object downward."""
        self.rect.y += self.speed
        self.update_hitbox()  # Update the hitbox position

    def draw(self, screen):
        """Draw the object on the screen."""
        screen.blit(self.image, self.rect)