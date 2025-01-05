import random
import json

def load_treasure_data(file):
    """Loads treasure room data from a JSON file."""
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def treasure_room():
    """Simulates the final treasure room challenge."""
    try:
        # Load treasure data
        treasure_data = load_treasure_data('data/TRClues.json')
        if not treasure_data:
            print("Error: Treasure data is empty or invalid.")
            return

        # Extract years and randomly select one
        years = list(treasure_data["Fort Boyard"].keys())
        selected_year = random.choice(years)

        # Extract shows for the selected year and randomly select one
        shows = list(treasure_data["Fort Boyard"][selected_year].keys())
        selected_show = random.choice(shows)

        # Retrieve clues and the code word
        selected_data = treasure_data["Fort Boyard"][selected_year][selected_show]
        clues = selected_data["Clues"]
        code_word = selected_data["CODE-WORD"].lower()

        print(f"Welcome to the treasure room! Year: {selected_year}, Show: {selected_show}")
        print("You must guess the code word to unlock the treasure.")
        print("Here are your first three clues:")
        for clue in clues[:3]:
            print(f"- {clue}")

        attempts = 3
        while attempts > 0:
            answer = input("Enter your guess for the code word: ").strip().lower()
            if answer == code_word:
                print("Congratulations! You've unlocked the treasure room!")
                return
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect! You have {attempts} attempt(s) remaining.")
                    if len(clues) > 3 + (3 - attempts):
                        print(f"Here is an additional clue: {clues[3 + (3 - attempts)]}")
                else:
                    print("You have used all your attempts!")
                    print(f"The correct code word was: {code_word}")
                    return
    except FileNotFoundError:
        print("Error: 'TRClues.json' file not found. Ensure it is in the 'data' directory.")
    except json.JSONDecodeError:
        print("Error: Failed to parse the JSON file. Ensure it is properly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    treasure_room()
