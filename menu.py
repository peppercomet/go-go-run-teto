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

        # Draw the title
        title_text = title_font.render("Go, go, run, Teto!", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Draw the best score
        best_score_text = font.render(f"Best Score: {best_score}", True, WHITE)
        best_score_rect = best_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(best_score_text, best_score_rect)

        # Draw unlocked achievements
        achievement_text = font.render("Unlocked Achievements:", True, WHITE)
        achievement_rect = achievement_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(achievement_text, achievement_rect)

        y_offset = 100
        for achievement_id in unlocked_achievements:
            # Look up the achievement details using the ID
            achievement = ACHIEVEMENTS.get(achievement_id)
            if achievement:
                achievement_name_text = font.render(achievement["name"], True, WHITE)
                achievement_name_rect = achievement_name_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
                screen.blit(achievement_name_text, achievement_name_rect)
                y_offset += 30

        # Draw the start option
        start_text = font.render("Press SPACE to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        screen.blit(start_text, start_rect)

        # Draw the quit option
        quit_text = font.render("Press Q to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4 + 50))
        screen.blit(quit_text, quit_rect)

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