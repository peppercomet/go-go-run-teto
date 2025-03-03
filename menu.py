import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_NAME, FONT_SIZE, ACHIEVEMENTS

def read_highest_score():
    """Read the highest score from the highest_score.txt file."""
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        # Return 0 if the file doesn't exist or contains invalid data
        return 0

def show_menu(screen, best_score, unlocked_achievements):
    """Display the main menu and return the user's choice."""

    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    title_font = pygame.font.Font(FONT_NAME, FONT_SIZE * 2)

    # Menu loop
    while True:
        screen.fill(BLACK)

        # Draw the title (moved higher)
        title_text = title_font.render("Go, go, run, Teto!", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))  
        screen.blit(title_text, title_rect)

        # Draw the best score (moved higher)
        best_score_text = font.render(f"Best Score: {best_score}", True, WHITE)
        best_score_rect = best_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))  
        screen.blit(best_score_text, best_score_rect)

        # Draw the start option (moved higher)
        start_text = font.render("Press SPACE to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) 
        screen.blit(start_text, start_rect)

        # Draw the quit option (moved higher)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  
        screen.blit(quit_text, quit_rect)

        # Draw "Unlocked Achievements:" on its own line
        achievements_label_text = font.render("Unlocked Achievements:", True, WHITE)
        achievements_label_rect = achievements_label_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(achievements_label_text, achievements_label_rect)

        # Split achievements into lines with a maximum of 3 achievements per line
        achievements_list = [ACHIEVEMENTS.get(achievement_id, {}).get("name", "") for achievement_id in unlocked_achievements]
        achievements_lines = []
        for i in range(0, len(achievements_list), 3):  # Split into chunks of 3
            achievements_lines.append(", ".join(achievements_list[i:i + 3]))

        # Draw each line of achievements
        y_offset = 130  # Starting y-offset for the first line of achievements
        for line in achievements_lines:
            achievements_text = font.render(line, True, WHITE)
            achievements_rect = achievements_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
            screen.blit(achievements_text, achievements_rect)
            y_offset += 30  # Increase y-offset for the next line

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