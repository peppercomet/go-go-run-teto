import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from menu import show_menu
from game_logic import GameLogic
from render import render_game_screen, render_game_over_screen
from achievements import load_achievements, save_achievement

# Initialize PyGame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Go, go, run!")

# Set up the clock
clock = pygame.time.Clock()

# Define game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_GAMEOVER = "gameover"

def main():
    # Initial game state
    game_state = STATE_MENU
    game_logic = None
    best_score = load_achievements()

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # State management
        if game_state == STATE_MENU:
            # Show the main menu and get the user's choice
            choice = show_menu(screen, best_score)
            if choice == "start":
                # Start a new game
                game_logic = GameLogic()
                game_state = STATE_PLAYING
            elif choice == "quit":
                running = False

        elif game_state == STATE_PLAYING:
            # Update game logic
            game_logic.update()

            # Render the game screen
            render_game_screen(screen, game_logic)

            # Check for game-over condition
            if game_logic.is_game_over():
                # Save the score if it's a new best
                if game_logic.score > best_score:
                    save_achievement(game_logic.score)
                    best_score = game_logic.score
                game_state = STATE_GAMEOVER

        elif game_state == STATE_GAMEOVER:
            # Render the game-over screen
            render_game_over_screen(screen, game_logic.score, best_score)

            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_logic = GameLogic()
                game_state = STATE_PLAYING
            elif keys[pygame.K_m]:
                game_state = STATE_MENU

        pygame.display.flip()

       
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()