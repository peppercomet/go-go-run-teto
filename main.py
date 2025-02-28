import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from menu import show_menu
from game_logic import GameLogic
from render import render_game_screen

# Initialize PyGame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Go, go, run, Teto!")

# Set up the clock
clock = pygame.time.Clock()

# Define game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"

def main():
    # Initial game state
    game_state = STATE_MENU
    game_logic = None

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
            choice = show_menu(screen, 0)  # Pass 0 as the best score for now
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
                game_state = STATE_MENU

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit PyGame
    pygame.quit()

if __name__ == "__main__":
    main()