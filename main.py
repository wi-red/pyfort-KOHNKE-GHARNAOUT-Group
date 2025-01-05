# Importing necessary modules and functions
from utility_functions import *  # Utility functions for team composition, menu handling, etc.
from math_challenges import *  # Mathematical challenge-related functions
from logical_challenges import *  # Logical challenge-related functions
from pere_fouras_challenge import *  # Père Fouras riddle challenge functions
from chance_challenges import *  # Games of chance challenge functions
from final_challenge import *  # Final treasure room challenge functions
import time  # For handling delays in game prompts
import os # For formatting the console



# Main game function
def game():
    os.system('cls') # Clears the console when starting the game
    keys = 0  # Counter to track the number of keys won
    print(introduction())  # Display the introduction to the game
    time.sleep(1.5)  # Pause for a short duration

    # Prompt the user to confirm readiness
    delay_print("Are you ready ? [Yes/No] ", 0.04)
    a = str(input(""))
    
    # Loop until a valid response is provided
    while a.lower() not in ["yes", "no", "y", "n"]:
        delay_print("Invalid input! You must answer by 'Yes' or 'No'! ", 0.05)
        delay_print("Are you ready ? [Yes/No] ", 0.02)
        a = str(input(""))
        print('\n')

    # Handle cases where the user is not ready
    if a.lower() in ["no", "n"]:
        delay_print("Take your time...\n", 0.04)
        time.sleep(2)
        delay_print("Just kidding, no time to waste!\n", 0.01)
        time.sleep(2)
        delay_print("(You can always scroll up for missed information)\n", 0.01)
        time.sleep(0.1)

    # Create a team for the game
    team = compose_equipe()
    print("\n")
    
    # Game loop: Continue until 3 keys are collected
    while keys < 3:
        challenge = challenges_menu()  # Display the menu and get the user's challenge choice
        current_player = choose_player(team)  # Select a player for the challenge
        
        # Execute the chosen challenge and check the result
        if challenge == 1:  # Mathematics challenge
            os.system('cls')
            if maths_challenge():
                current_player['keys_won'] += 1
                keys += 1
        elif challenge == 2:  # Logic challenge
            os.system('cls')
            if battleship_game():
                current_player['keys_won'] += 1
                keys += 1
        elif challenge == 3:  # Chance challenge
            os.system('cls')
            if chance_challenge():
                current_player['keys_won'] += 1
                keys += 1
        elif challenge == 4:  # Père Fouras' riddle
            os.system('cls')
            if pere_fouras_riddles():
                current_player['keys_won'] += 1
                keys += 1
        
            print(f'You now have {keys} keys in total! Only {3 - keys} keys left to get to the treasure room!\n')
    # When 3 keys are collected, proceed to the treasure room
    print("You now have 3 keys! You can now go to the Treasure Room.")
    time.sleep(2)
    os.system('cls')
    if treasure_room()==True:  # Final challenge to unlock the treasure
        return "\nYou have won Fort Boyard!"
    else:
        return "Oh no! You have lost Fort Boyard! Better luck next time!"

# Entry point of the script
if __name__ == "__main__":
    result = game()
    print(result)
