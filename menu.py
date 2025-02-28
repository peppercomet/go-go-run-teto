import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FONT_NAME, FONT_SIZE

def show_menu(screen, best_score):
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    title_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE * 2)

    # Menu loop
    while True:
        screen.fill(BLACK)

        # Draw the title
        title_text = title_font.render("Go, go, run!", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Draw the best score
        best_score_text = font.render(f"Best Score: {best_score}", True, WHITE)
        best_score_rect = best_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(best_score_text, best_score_rect)

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