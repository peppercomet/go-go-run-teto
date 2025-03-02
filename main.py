import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ACHIEVEMENTS, ACHIEVEMENTS_FILE, SOUNDTRACK_FILE
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

def load_achievements():
    """Load unlocked achievements from the achievements file."""
    try:
        with open(ACHIEVEMENTS_FILE, "r") as file:
            return set(file.read().splitlines())  # Use a set for fast lookups
    except FileNotFoundError:
        return set()  # Return an empty set if the file doesn't exist

def save_achievement(achievement_id):
    """Save a newly unlocked achievement to the achievements file."""
    with open(ACHIEVEMENTS_FILE, "a") as file:
        file.write(achievement_id + "\n")  # Append the achievement ID to the file

def check_achievements(score, objects_collected, time_survived, unlocked_achievements):
    """Check if any new achievements have been unlocked."""
    new_achievements = []
    for achievement_id, achievement in ACHIEVEMENTS.items():
        if achievement_id not in unlocked_achievements and achievement["condition"](score, objects_collected, time_survived):
            new_achievements.append(achievement_id)  # Add newly unlocked achievements to the list
    return new_achievements

def main():
    # Load unlocked achievements
    unlocked_achievements = load_achievements()

    # Load the soundtrack
    pygame.mixer.music.load(SOUNDTRACK_FILE)
    pygame.mixer.music.set_volume(0.3)  # Set volume to 30% (adjust as needed)

    # Initial game state
    game_state = STATE_MENU
    game_logic = None
    best_score = 0  # Track the best score across sessions

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
            choice = show_menu(screen, best_score, unlocked_achievements)  # Pass best score and achievements
            if choice == "start":
                # Start a new game
                game_logic = GameLogic()
                game_state = STATE_PLAYING
                pygame.mixer.music.play(-1)  # Play the soundtrack on loop
            elif choice == "quit":
                running = False

        elif game_state == STATE_PLAYING:
            # Update game logic
            game_logic.update()

            # Render the game screen
            render_game_screen(screen, game_logic)

            # Check for game-over condition
            if game_logic.is_game_over():
                # Calculate time survived
                time_survived = game_logic.get_time_survived()

                # Check for new achievements
                new_achievements = check_achievements(
                    game_logic.score,
                    game_logic.objects_collected,
                    time_survived,
                    unlocked_achievements
                )

                # Save new achievements to the file and add them to the unlocked set
                for achievement_id in new_achievements:
                    save_achievement(achievement_id)  # Save immediately to the file
                    unlocked_achievements.add(achievement_id)  # Add to the in-memory set

                # Update the best score
                if game_logic.score > best_score:
                    best_score = game_logic.score

                # Stop the soundtrack and return to the menu
                pygame.mixer.music.stop()
                game_state = STATE_MENU

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit PyGame
    pygame.quit()

if __name__ == "__main__":
    main()