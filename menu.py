import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_NAME, FONT_SIZE, ACHIEVEMENTS

def show_menu(screen, best_score, unlocked_achievements):
    """Display the main menu and return the user's choice."""
    # Load the custom font
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    title_font = pygame.font.Font(FONT_NAME, FONT_SIZE * 2)

    # Menu loop
    while True:
        screen.fill(BLACK)

        # Draw the title (moved higher)
        title_text = title_font.render("Go, go, run, Teto!", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))  # Adjusted y-position
        screen.blit(title_text, title_rect)

        # Draw the best score (moved higher)
        best_score_text = font.render(f"Best Score: {best_score}", True, WHITE)
        best_score_rect = best_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))  # Adjusted y-position
        screen.blit(best_score_text, best_score_rect)

        # Draw the start option (moved higher)
        start_text = font.render("Press SPACE to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Adjusted y-position
        screen.blit(start_text, start_rect)

        # Draw the quit option (moved higher)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  # Adjusted y-position
        screen.blit(quit_text, quit_rect)

        # Draw "Unlocked Achievements:" on its own line
        achievements_label_text = font.render("Unlocked Achievements:", True, WHITE)
        achievements_label_rect = achievements_label_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))  # Adjusted y-position
        screen.blit(achievements_label_text, achievements_label_rect)

        # Draw the actual achievements on the next line
        achievements_str = ", ".join(
            [ACHIEVEMENTS.get(achievement_id, {}).get("name", "") for achievement_id in unlocked_achievements]
        )
        achievements_text = font.render(achievements_str, True, WHITE)
        achievements_rect = achievements_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))  # Adjusted y-position
        screen.blit(achievements_text, achievements_rect)

        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "start"
                if event.key == pygame.K_q:
                    return "quit"