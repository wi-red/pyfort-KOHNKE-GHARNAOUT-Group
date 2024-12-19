import random

def shell_game():
    # Initialize the list of shells
    shells = ['A', 'B', 'C']
    attempts = 0
    max_attempts = 2
    
    print("Welcome to the Shell Game!")
    print(f"Try to guess which shell hides the key. You have {max_attempts} attempts.")
    
    # Randomly select the shell hiding the key
    key_shell = random.choice(shells)
    
    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1}/{max_attempts}")
        print(f"Shells: {', '.join(shells)}")
        
        # Ask the player to choose a shell
        player_choice = input("Choose a shell (A, B, or C): ").strip().upper()
        
        if player_choice in shells:
            if player_choice == key_shell:
                print("Congratulations! You found the key under the shell!")
                return True
            else:
                print("Wrong guess. Try again.")
        else:
            print("Invalid choice. Please select A, B, or C.")
        
        attempts += 1
    
    # If the player exhausts all attempts
    print("\nSorry, you've lost the game.")
    print(f"The key was under shell {key_shell}.")
    return False


def roll_dice_game():
    max_attempts = 3
    dices={
        1 : 
}
    print("Welcome to the Rolling Dice Game!")
    print("The first to roll a 6 wins the game. You have 3 attempts.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}/{max_attempts}")
        
        # Player's turn
        input("Press 'Enter' to roll the dice...")
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Player rolled: {player_dice}")
        
        if 6 in player_dice:
            print("Congratulations! You rolled a 6 and won the game!")
            return True

        # Game master's turn
        game_master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Game Master rolled: {game_master_dice}")
        
        if 6 in game_master_dice:
            print("The Game Master rolled a 6. You lost the game.")
            return False

        print("No one rolled a 6. Moving to the next attempt...")

    # If no one rolls a 6 after all attempts
    print("\nNeither you nor the Game Master rolled a 6. The game is a draw.")
    return False


if __name__ == "__main__":
    shell_game()
    roll_dice_game()
