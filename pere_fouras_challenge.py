

import json

def load_riddles(file):

        # Open the file in read mode with UTF-8 encoding
        with open(file, 'r', encoding='utf-8') as f:
            riddles = json.load(f)

        return riddles

import random

def pere_fouras_riddles():
  
    # Load the riddles from the file
    riddles = load_riddles('data/PFRiddles.json')
    if not riddles:
        print("No riddles available. Ensure the file is properly formatted and present.")
        return False

    # Randomly select a riddle from the list
    selected_riddle = random.choice(riddles)
    question = selected_riddle.get('question')
    correct_answer = selected_riddle.get('answer', '').lower()

    if not question or not correct_answer:
        print("The selected riddle is malformed. Ensure each riddle has 'question' and 'answer'.")
        return False

    print("\nPère Fouras: Here is your riddle:")
    print(f"\"{question}\"")
    
    # Initialize attempts and success flag
    attempts = 3
    success = False

    # Game loop for up to 3 attempts
    while attempts > 0:
        player_answer = input("\nYour answer: ").strip().lower()
        if player_answer == correct_answer:
            print("Père Fouras: Congratulations !! That is the correct answer. You win a key!")
            success = True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Père Fouras: Incorrect! You have {attempts} attempt(s) left becareful !.")
            else:
                print(f"Père Fouras: Out of attempts! The correct answer was \"{correct_answer}\".")

    return success



if __name__ == "__main__":
    pere_fouras_riddles()

