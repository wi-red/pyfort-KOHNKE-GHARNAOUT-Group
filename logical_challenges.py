# Battleship Game Implementation
import random

def next_player(player):
    """Returns the index of the next player."""
    return 1 - player

def empty_grid():
    """Generates and returns an empty 3x3 grid."""
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid(grid, message):
    """Displays the grid with a message."""
    print(message)
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def ask_position():
    """Asks the user for a position on the grid."""
    while True:
        try:
            position = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ")
            row, col = map(int, position.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid format. Please use the format row,column.")

def initialize():
    """Initializes the player's grid by placing two boats."""
    grid = empty_grid()
    for i in range(2):
        while True:
            print(f"Boat {i + 1}")
            row, col = ask_position()
            if grid[row][col] == " ":
                grid[row][col] = "B"
                break
            else:
                print("Position already occupied. Choose another.")
    return grid

def turn(player, player_shots_grid, opponent_grid):
    """Handles a player's turn."""
    display_grid(player_shots_grid, "History of your previous shots:")
    print(f"Player {player + 1}, it's your turn to shoot!")
    while True:
        row, col = ask_position()
        if player_shots_grid[row][col] == " ":
            if opponent_grid[row][col] == "B":
                print("Hit, sunk!")
                player_shots_grid[row][col] = "x"
                opponent_grid[row][col] = "x"
            else:
                print("Splash...")
                player_shots_grid[row][col] = "."
            break
        else:
            print("You already shot there. Try another position.")

def has_won(player_shots_grid):
    """Checks if all boats on the opponent's grid have been sunk."""
    return sum(row.count("x") for row in player_shots_grid) == 2

def battleship_game():
    """Orchestrates the entire Battleship game."""
    print("Welcome to Battleship! Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B', missed shots by '.', and hits by 'x'.")

    # Player 1 initialization
    print("Player 1, place your boats:")
    player1_grid = initialize()

    # Player 2 initialization
    print("Player 2, place your boats:")
    player2_grid = initialize()

    # Empty shot grids
    player1_shots = empty_grid()
    player2_shots = empty_grid()

    current_player = 0
    while True:
        if current_player == 0:
            turn(0, player1_shots, player2_grid)
            if has_won(player1_shots):
                print("Player 1 wins!")
                break
        else:
            turn(1, player2_shots, player1_grid)
            if has_won(player2_shots):
                print("Player 2 wins!")
                break
        current_player = next_player(current_player)

if __name__ == "__main__":
    battleship_game()
