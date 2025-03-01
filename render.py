import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_NAME, FONT_SIZE, BACKGROUND_IMAGE, NEON_RED, NEON_GREEN

def render_game_screen(screen, game_logic):
    """Render the game screen."""
    # Draw the background
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))

    # Draw the player
    game_logic.player.draw(screen)

    # Draw the falling objects
    for obj in game_logic.objects:
        obj.draw(screen)

    # Load the custom font
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)

    # Draw the score
    score_label = font.render("Score: ", True, WHITE)  
    score_value = font.render(f"{game_logic.score}", True, NEON_GREEN)  
    score_label_pos = (10, 10)  # Position for "Score:"
    score_value_pos = (score_label_pos[0] + score_label.get_width(), 10)  
    screen.blit(score_label, score_label_pos)
    screen.blit(score_value, score_value_pos)

    # Draw the lives
    lives_label = font.render("Lives: ", True, WHITE)
    lives_value = font.render(f"{game_logic.lives}", True, NEON_RED)  
    lives_label_pos = (10, 50)  # Position for "Lives:"
    lives_value_pos = (lives_label_pos[0] + lives_label.get_width(), 50)  
    screen.blit(lives_label, lives_label_pos)
    screen.blit(lives_value, lives_value_pos)

    # Update the display
    pygame.display.flip()