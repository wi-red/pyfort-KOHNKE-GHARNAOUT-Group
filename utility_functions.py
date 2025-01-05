import time  # Importing the time module for adding delays in text output
import sys  # Importing the sys module for managing text output to the console

def introduction():
    """
    Provides an introductory message explaining the game's objective.
    :return: A string containing the introduction message.
    """
    delay_print("Hello player!\n\n",.05)
    time.sleep(1.5)
    delay_print("Your goal is to access the treasure room. In order to do that you and your team will have to earn 3 keys by completing challenges.\n\n",.03)
    time.sleep(1.5)
    delay_print("Good Luck !\n[...",.04)
    return ']'

def compose_equipe():
    """
    Allows the user to create a team of 1 to 3 players.
    Each player has attributes: name, profession, leader status, and keys won.
    :return: A list of dictionaries representing the team.
    """
    print("\n------Team Composition------\n")
    team = []  # List to store team members
    c = 0  # Counter to track if a leader is assigned
    while True:
        try:
            # Ask the user how many players are in the team
            equipe = int(input("How many players are on the team? [1-3] : "))
            print("\n")
            
            # Validate the number of players (must be between 1 and 3)
            while equipe < 1 or equipe > 3:
                if equipe < 1:
                    print("Invalid value! Your team must have at least one player!\n")
                elif equipe > 3:
                    print("Invalid value! Your team must have 3 players at maximum!\n")
                equipe = int(input("How many players are on the team? [1-3] : "))
            
            # Gather information for each player
            for i in range(equipe):
                print(f"------PLAYER {i + 1}------")
                delay_print("Enter your name: ", .04)
                name = str(input(""))
                delay_print("Enter your profession: ", .04)
                profession = str(input(""))

                # Assign leader role to one player
                leader = False
                if c < 1:
                    delay_print("Are you the team leader? [Yes/No]: ", .04)
                    leader_Q = str(input("")).strip().lower()
                    
                    # Validate the input for leader assignment
                    while leader_Q not in ["yes", "no", "y", "n"]:
                        delay_print("Invalid Input! Your answer should be 'Yes' or 'No'! ", .02)
                        delay_print("Are you the team leader? [Yes/No]: ", .02)
                        leader_Q = str(input("")).strip().lower()
                    
                    # Assign leader status based on input
                    if leader_Q in ["yes", "y"]:
                        leader = True
                        c += 1

                team.append({'Name': name, 'Profession': profession, 'Leader': leader, 'keys_won': 0})
            
            # If no leader was assigned, make Player 1 the leader by default
            if c == 0:
                delay_print("\nPlayer 1 has been designated as the leader by default.\n", .02)
                team[0]["Leader"] = True

            return team  # Return the composed team

        except ValueError:
            print("Your value should be an integer. Please try again.")

def compose_equipe_no_print():
    """
    A placeholder function to allow team composition without printed output.
    Calls `compose_equipe` internally.
    """
    compose_equipe()
    return

def delay_print(s, speed):
    """
    Prints a string character by character with a delay between each character.
    :param s: The string to print.
    :param speed: The delay in seconds between each character.
    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)

def challenges_menu():
    """
    Displays a menu for the user to select a type of challenge.
    :return: An integer corresponding to the user's choice of challenge.
    """
    print("------Challenge Selection------\n")
    delay_print("You must now choose a challenge.\n\n"
                "1. Mathematics Challenge\n"
                "2. Logic Challenge\n"
                "3. Chance Challenge\n"
                "4. Père Fouras' riddle\n\n"
                "Your choice is: ", .02)
    a = int(input(""))  # User inputs their choice
    
    # Display the chosen challenge type
    if a == 1:
        print("You chose the Mathematics Challenge!")
    elif a == 2:
        print("You chose the Logic Challenge!")
    elif a == 3:
        print("You chose the Chance Challenge!")
    elif a == 4:
        print("You chose the Père Fouras' riddle!")
    return a

def choose_player(team):
    """
    Allows the user to select a player from the team for a challenge.
    Displays the team members and their details.
    :param team: A list of dictionaries representing the team.
    :return: The selected player's dictionary.
    """
    # Display team members with their attributes
    for i in range(len(team)):
        if team[i]["Leader"]:
            delay_print(f'{i + 1}. {team[i]["Name"]} ({team[i]["Profession"]}) - Leader',.02)
        else:
            delay_print(f'{i + 1}. {team[i]["Name"]} ({team[i]["Profession"]}) - Member',.02)
    
    # Prompt the user to select a player
    a = int(input("Enter the player's number: "))
    while a < 1 or a > len(team):  # Validate the input
        print(f"Invalid Value! The player's number must be between 1 and {len(team)}")
        a = int(input("Enter the player's number: "))
    
    return team[a - 1]  # Return the selected player's dictionary

# Example team for testing
random_team = [{'Name': 'A', 'Profession': 'A', 'Leader': False, 'keys_won': 0}, 
               {'Name': 'B', 'Profession': 'B', 'Leader': True, 'keys_won': 0}]

# Main script for testing the functions
if __name__ == "__main__":
    print(introduction())  # Display introduction
    team = compose_equipe()  # Compose the team
    challenge = challenges_menu()  # Select a challenge
    player = choose_player(team)  # Choose a player
