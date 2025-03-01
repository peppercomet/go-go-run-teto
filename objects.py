import pygame
import random
from settings import SCREEN_WIDTH, OBJECT_SPEED, OBJECT_WIDTH, OBJECT_HEIGHT, GOOD_OBJECT_IMAGE

class FallingObject:
    def __init__(self):
        self.image = pygame.image.load(GOOD_OBJECT_IMAGE)
        self.image = pygame.transform.scale(self.image, (OBJECT_WIDTH, OBJECT_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect.y = -OBJECT_HEIGHT  # Start above the screen
        self.speed = OBJECT_SPEED

    def update(self):
        """Move the object downward."""
        self.rect.y += self.speed

    def draw(self, screen):
        """Draw the object on the screen."""
        screen.blit(self.image, self.rect)