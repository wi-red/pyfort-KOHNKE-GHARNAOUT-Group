import json
import random

def treasure_room():
    # Step 1: Load the data from 'TRClues.json'
    with open('TRClues.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Step 2: Randomly select a program
    programs = list(data.values())  # Extract the list of programs

    selected_program = random.choice(programs)
    clues = selected_program.get("clues", [])
    codeword = selected_program.get("codeword", "").lower()

    if not clues or not codeword:
        print("The selected program does not contain valid clues or a codeword.")
        return

    # Step 3: Display the first three clues
    print("\nWelcome to the Treasure Room!")
    print("Here are your first three clues:")
    for clue in clues[:3]:
        print(f"- {clue}")

    # Step 4: Player attempts to guess the codeword
    attempts = 3
    success = False

    while attempts > 0:
        player_answer = input("\nEnter your guess for the codeword: ").strip().lower()
        if player_answer == codeword:
            success = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempt(s) remaining.")
                if len(clues) > 3 + (3 - attempts):  # Provide additional clues if available
                    print(f"Additional clue: {clues[3 + (3 - attempts)]}")
            else:
                print(f"Out of attempts! The correct codeword was: \"{codeword}\".")

    # Step 6: Final message
    if success:
        print("\nCongratulations! You successfully guessed the codeword and accessed the treasure!")
    else:
        print("\nYou failed to guess the codeword. Better luck next time!")
