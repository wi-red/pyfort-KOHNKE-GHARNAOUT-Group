import random  # Importing the random module for random selections
import json  # Importing the json module to handle JSON file operations

def load_treasure_data(file):
    """
    Loads treasure room data from a JSON file.
    :param file: The path to the JSON file containing treasure room data.
    :return: A dictionary containing the parsed data.
    """
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def treasure_room():
    """
    Simulates the final treasure room challenge.
    The player must guess the code word to unlock the treasure room,
    using clues provided from the data file.
    :return: True if the player guesses the code word correctly, False otherwise.
    """
    print("------Treasure Room------")
    try:
        # Load treasure data from a predefined JSON file
        treasure_data = load_treasure_data('data/TRClues.json')
        if not treasure_data:  # Check if the data is valid
            print("Error: Treasure data is empty or invalid.")
            return

        # Extract the available years and randomly select one
        years = list(treasure_data["Fort Boyard"].keys())
        selected_year = random.choice(years)

        # Extract the shows for the selected year and randomly select one
        shows = list(treasure_data["Fort Boyard"][selected_year].keys())
        selected_show = random.choice(shows)

        # Retrieve the clues and the code word for the selected show
        selected_data = treasure_data["Fort Boyard"][selected_year][selected_show]
        clues = selected_data["Clues"]  # List of clues
        code_word = selected_data["CODE-WORD"].lower()  # Convert the code word to lowercase for case-insensitive comparison

        # Display introductory information for the treasure room challenge
        print(f"Welcome to the treasure room! Year: {selected_year}, Show: {selected_show}")
        print("You must guess the code word to unlock the treasure.")
        print("Here are your first three clues:")
        for clue in clues[:3]:  # Show the first three clues initially
            print(f"- {clue}")

        attempts = 3  # Initialize the number of attempts
        while attempts > 0:
            # Prompt the player to guess the code word
            answer = input("Enter your guess for the code word: ").strip().lower()
            if answer == code_word:
                # If the guess is correct, congratulate the player
                print("\nCongratulations! You've unlocked the treasure room!")
                return True
            else:
                attempts -= 1  # Decrement the number of attempts
                if attempts > 0:
                    print(f"Incorrect! You have {attempts} attempt(s) remaining.")
                    # Provide an additional clue if available
                    if len(clues) > 3 + (3 - attempts):
                        print(f"Here is an additional clue: {clues[3 + (3 - attempts)]}")
                else:
                    # If no attempts remain, reveal the correct code word
                    print("You have used all your attempts!")
                    print(f"The correct code word was: {code_word}")
                    return False
    except json.JSONDecodeError:
        # Handle JSON file parsing errors
        print("Error: Failed to parse the JSON file. Ensure it is properly formatted.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Main script for testing the treasure_room function
if __name__ == "__main__":
    treasure_room()
