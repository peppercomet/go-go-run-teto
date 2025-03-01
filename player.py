import pygame
from settings import PLAYER_IMAGE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_START_X, PLAYER_START_Y, SCREEN_WIDTH, PLAYER_HITBOX_WIDTH, PLAYER_HITBOX_HEIGHT

class Player:
    def __init__(self):
        # Load the player image
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define the player's initial position
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = PLAYER_START_Y

        # Player movement settings
        self.speed = 9  # Maximum speed
        self.acceleration = 0.5  # How quickly the player speeds up
        self.friction = 0.3  # How quickly the player slows down
        self.velocity_x = 0  # Current horizontal velocity

        # Define the hitbox (smaller than the image rectangle)
        self.hitbox = pygame.Rect(0, 0, PLAYER_HITBOX_WIDTH, PLAYER_HITBOX_HEIGHT)
        self.update_hitbox()  # Position the hitbox correctly

    def update_hitbox(self):
        """Update the hitbox position to align with the player's position."""
        self.hitbox.center = self.rect.center

    def move_left(self):
        """Accelerate the player to the left."""
        self.velocity_x -= self.acceleration
        if self.velocity_x < -self.speed:  # Cap the speed
            self.velocity_x = -self.speed

    def move_right(self):
        """Accelerate the player to the right."""
        self.velocity_x += self.acceleration
        if self.velocity_x > self.speed:  # Cap the speed
            self.velocity_x = self.speed

    def apply_friction(self):
        """Apply friction to slow down the player."""
        if self.velocity_x > 0:
            self.velocity_x -= self.friction
            if self.velocity_x < 0:
                self.velocity_x = 0
        elif self.velocity_x < 0:
            self.velocity_x += self.friction
            if self.velocity_x > 0:
                self.velocity_x = 0

    def update(self):
        """Update the player's position based on velocity."""
        self.rect.x += self.velocity_x

        # Prevent the player from moving off the screen
        if self.rect.x < 0:
            self.rect.x = 0
            self.velocity_x = 0  # Stop sliding
        elif self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH
            self.velocity_x = 0  # Stop sliding

        self.update_hitbox()  # Update the hitbox position

    def handle_input(self, keys):
        """Handle player movement based on keyboard input."""
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

        # Apply friction when no keys are pressed
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.apply_friction()

    def check_collision(self, object_rect):
        """Check if the player collides with an object using the hitbox."""
        return self.hitbox.colliderect(object_rect)

    def draw(self, screen):
        """Draw the player on the screen."""
        screen.blit(self.image, self.rect)