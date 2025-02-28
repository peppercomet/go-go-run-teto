import pygame
from settings import PLAYER_IMAGE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_START_X, PLAYER_START_Y, SCREEN_WIDTH

class Player:
    def __init__(self):
        # Load the player image
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define the player's initial position
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = PLAYER_START_Y

        # Player movement speed
        self.speed = 5

    def move_left(self):
        """Move the player to the left."""
        self.rect.x -= self.speed
        # Prevent the player from moving off the left side of the screen
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        """Move the player to the right."""
        self.rect.x += self.speed
        # Prevent the player from moving off the right side of the screen
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

    def handle_input(self, keys):
        """Handle player movement based on keyboard input."""
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

    def check_collision(self, object_rect):
        """Check if the player collides with an object."""
        return self.rect.colliderect(object_rect)

    def draw(self, screen):
        """Draw the player on the screen."""
        screen.blit(self.image, self.rect)