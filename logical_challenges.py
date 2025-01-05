import random  # Importing the random module for generating random positions

def next_player(player):
    """
    Switches to the other player.
    :param player: The index of the current player (0 or 1).
    :return: The index of the next player (1 or 0).
    """
    return 1 - player

def empty_grid():
    """
    Creates and returns a 3x3 empty grid.
    :return: A 3x3 list filled with spaces (" ").
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid(grid, message):
    """
    Displays the grid with a contextual message.
    :param grid: The grid to display (3x3 list).
    :param message: A string providing context about the displayed grid.
    """
    print(message)
    for row in grid:
        print(" | ".join(row))  # Join row elements with a vertical bar
        print("-" * 9)  # Separator between rows

def ask_position():
    """
    Prompts the user for a valid position on the grid.
    Ensures the input is within bounds and correctly formatted.
    :return: A tuple (row, col) representing the 0-based grid position.
    """
    while True:
        try:
            position = input("Enter a position (row,column) [1-3]: ")  # Prompt for input
            row, col = map(int, position.split(","))  # Parse input into row and column
            row, col = row - 1, col - 1  # Convert to 0-based indexing
            if 0 <= row < 3 and 0 <= col < 3:  # Check bounds
                return row, col
            else:
                print("Position out of bounds. Please try again.")
        except (ValueError, IndexError):  # Handle invalid input format
            print("Invalid format. Please enter in the format row,column (e.g., 1,2).")

def initialize():
    """
    Initializes the player's grid by placing 2 boats.
    :return: A 3x3 grid with boats ("B") placed.
    """
    grid = empty_grid()  # Start with an empty grid
    boats_placed = 0
    print("Place your 2 boats on the grid.")
    while boats_placed < 2:
        row, col = ask_position()  # Get boat position from user
        if grid[row][col] == " ":
            grid[row][col] = "B"  # Mark the position with a boat
            boats_placed += 1
            display_grid(grid, "Your grid after placing a boat:")
        else:
            print("That position is already occupied. Choose another.")
    return grid

def turn(player, player_shots_grid, opponent_grid):
    """
    Handles a single turn for the current player.
    :param player: The index of the current player (0 for human, 1 for game master).
    :param player_shots_grid: The current player's shot grid.
    :param opponent_grid: The opponent's grid containing boat positions.
    """
    if player == 0:  # Human player's turn
        print("Your turn!")
        display_grid(player_shots_grid, "Your shot history:")
        while True:
            row, col = ask_position()  # Get shot position
            if player_shots_grid[row][col] == " ":
                break  # Valid shot position
            else:
                print("You already shot there. Try again.")
    else:  # Game master's turn
        print("Game master's turn!")
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)  # Random shot
            if player_shots_grid[row][col] == " ":
                break

    # Check if the shot hits a boat
    if opponent_grid[row][col] == "B":
        print("Hit!")
        player_shots_grid[row][col] = "x"  # Mark hit on shot grid
        opponent_grid[row][col] = "x"  # Mark hit on opponent's grid
    else:
        print("Miss!")
        player_shots_grid[row][col] = "."  # Mark miss on shot grid

def has_won(player_shots_grid):
    """
    Checks if all opponent boats are sunk.
    :param player_shots_grid: The current player's shot grid.
    :return: True if all boats are sunk, False otherwise.
    """
    return sum(row.count("x") for row in player_shots_grid) == 2  # 2 boats sunk

def battleship_game():
    """
    Orchestrates the Battleship game.
    Players alternate turns trying to sink each other's boats.
    :return: True if the human player wins, False otherwise.
    """
    print("Welcome to Battleship! Place 2 boats on your 3x3 grid. Sink all enemy boats to win!")

    # Initialize grids for the human player and the game master
    player_grid = initialize()
    game_master_grid = empty_grid()

    # Randomly place 2 boats on the game master's grid
    game_master_boats = 0
    while game_master_boats < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == " ":
            game_master_grid[row][col] = "B"
            game_master_boats += 1

    # Create empty shot grids for both players
    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    # Game loop
    current_player = 0  # Human player starts
    while True:
        if current_player == 0:  # Human player's turn
            turn(0, player_shots_grid, game_master_grid)
            if has_won(player_shots_grid):  # Check if human player wins
                print("Congratulations! You have won a key!")
                return True
        else:  # Game master's turn
            turn(1, game_master_shots_grid, player_grid)
            if has_won(game_master_shots_grid):  # Check if game master wins
                print("The game master has won! Better luck next time!")
                return False

        current_player = next_player(current_player)  # Switch turns
