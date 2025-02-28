import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_NAME, FONT_SIZE, BACKGROUND_IMAGE

def render_game_screen(screen, game_logic):
    """Render the game screen."""
    # Draw the background
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))

    # Draw the player
    game_logic.player.draw(screen)

    # Load the custom font
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)

    # Draw the score and lives
    score_text = font.render(f"Score: {game_logic.score}", True, WHITE)
    lives_text = font.render(f"Lives: {game_logic.lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update the display
    pygame.display.flip()