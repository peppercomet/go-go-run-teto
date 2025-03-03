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
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set() 

def save_achievement(achievement_id):
    """Save a newly unlocked achievement to the achievements file."""
    with open(ACHIEVEMENTS_FILE, "a") as file:
        file.write(achievement_id + "\n")

def check_achievements(score, objects_collected, time_survived, unlocked_achievements):
    """Check if any new achievements have been unlocked."""
    new_achievements = []
    for achievement_id, achievement in ACHIEVEMENTS.items():
        if achievement_id not in unlocked_achievements and achievement["condition"](score, objects_collected, time_survived):
            new_achievements.append(achievement_id)
    return new_achievements

def read_highest_score():
    """Read the highest score from the highest_score.txt file."""
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    """Save the high score to the highest_score.txt file if it's higher than the current one."""
    try:
        # Check if the current score is higher than the saved high score
        current_high_score = read_highest_score()
        
        # Only save if the new score is higher
        if score > current_high_score:
            with open("highest_score.txt", "w") as file:
                file.write(str(score))
            return True
        return False
    except Exception as e:
        print(f"Error saving high score: {e}")
        return False

def main():
    # Load unlocked achievements
    unlocked_achievements = load_achievements()

    # Load the soundtrack
    pygame.mixer.music.load(SOUNDTRACK_FILE)
    pygame.mixer.music.set_volume(0.3)

    # Initial game state
    game_state = STATE_MENU
    game_logic = None
    best_score = read_highest_score()

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
            choice = show_menu(screen, best_score, unlocked_achievements)
            if choice == "start":
                # Start a new game
                game_logic = GameLogic()
                game_state = STATE_PLAYING
                pygame.mixer.music.play(-1)
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
                    save_high_score(best_score)  # Save the new best score to the file

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