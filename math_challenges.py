import random  # Importing the random module for generating random numbers

#----------------FACTORIAL GAME----------------#
def factorial(n):
    """
    Calculates the factorial of a given number n.
    :param n: Integer for which the factorial is calculated.
    :return: The factorial of n.
    """
    N = 1
    if n > 0:
        for i in range(0, n):
            N = N * (n - i)  # Multiply progressively to calculate factorial
    return N

def math_challenge_factorial():
    """
    Conducts the Factorial Game.
    Generates a random number and prompts the user to calculate its factorial.
    Provides feedback and returns True if the answer is correct, otherwise False.
    """
    print("\n#----------------FACTORIAL GAME----------------#\n")
    print("Welcome to the Factorial Game!")
    n = random.randint(1, 10)  # Generate a random number between 1 and 10
    print(f"\nMath challenger: Calculate the factorial of {n}.\n")
    
    X = None
    X_int = False

    # Input validation loop to ensure user enters an integer
    while not X_int:
        try:
            X = int(input("Your answer is: "))
            print(" ")
            X_int = True
        except ValueError:
            print("Your answer should be an integer! Please try again.")

    # Check if the user's answer matches the calculated factorial
    if X == factorial(n):
        print("Correct answer! You've won a key.\n")
        return True
    else:
        print("Wrong answer... Better luck next time.\n")
        return False


#----------------PRIME GAME----------------#

def is_prime(n):
    """
    Checks if a given number n is a prime number.
    :param n: Integer to check for primality.
    :return: True if n is prime, False otherwise.
    """
    c = 0  # Counter for divisors
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c <= 2  # Prime numbers have only two divisors: 1 and itself

def nearest_prime(n):
    """
    Finds the nearest prime number greater than or equal to n.
    :param n: Starting integer to find the nearest prime.
    :return: The nearest prime number.
    """
    c = n + 1
    while not is_prime(c):
        c += 1
    return c

def match_challenge_prime():
    """
    Conducts the Prime Game.
    Generates a random number and asks the user to find the nearest prime number.
    Provides feedback and returns True if the answer is correct, otherwise False.
    """
    print("\n#----------------PRIME GAME----------------#\n")
    print("Welcome to the Prime Game!")
    N = random.randint(10, 20)  # Generate a random number between 10 and 20
    X_int = False
    print(f"\nMath Challenge: Find the nearest prime to {N}.\n")

    # Input validation loop to ensure user enters an integer
    while not X_int:
        try:
            X = int(input("Your answer is : "))
            print(" ")
            if X == nearest_prime(N):  # Check if the user's answer is correct
                print("Correct answer! You've won a key\n")
                return True
            else:
                print("Wrong answer... Better luck next time!\n")
                return False
        except ValueError:
            print("\nYour value should be an integer! Please try again.")


#----------------MATH ROULETTE GAME----------------#
def math_roulette_challenge():
    """
    Conducts the Math Roulette Game.
    Generates random numbers and selects a random operation (addition, subtraction, multiplication).
    Asks the user to calculate the result of the operation on the numbers.
    Provides feedback and returns True if the answer is correct, otherwise False.
    """
    print("\n#----------------MATH ROULETTE GAME----------------#\n")
    L1 = ['*', '+', '-']  # List of possible operations
    L2 = []  # List to hold random numbers
    X_int = False
    print("Welcome to the Roulette Game!")

    # Generate 5 random numbers between 1 and 20
    for i in range(5):
        L2.append(random.randint(1, 20))

    op = L1[random.randint(0, 2)]  # Randomly choose an operation

    # Perform the operation based on the random choice
    if op == "*":
        print("\nCalculate the result by combining these numbers with multiplication\n")
        result = L2[0]
        for i in range(1, 5):
            result *= L2[i]
    elif op == '+':
        result = L2[0]
        print("Calculate the result by combining these numbers with addition\n")
        for i in range(1, 5):
            result += L2[i]
    elif op == '-':
        result = L2[0]
        print("Calculate the result by combining these numbers with subtraction\n")
        for i in range(1, 5):
            result -= L2[i]

    print("|TESTING ONLY| ANSWER IS:", result)  # Debugging hint (to be removed in production)
    print("Numbers on the roulette:", L2, "\n")

    # Input validation loop to ensure user enters an integer
    while not X_int:
        try:
            X = int(input("Your answer is: "))
            print(" ")
            if X == result:  # Check if the user's answer is correct
                print("Correct answer! You've won a key\n")
                return True
            else:
                print("Wrong answer... Better luck next time!\n")
                return False
        except ValueError:
            print("\nYour value should be an integer! Please try again.\n")


def maths_challenge():
    """
    Randomly selects and executes one of the math challenges: Factorial, Prime, or Roulette.
    """
    challenges = ["factorial", "prime", "roulette"]
    z = challenges[random.randint(0, 2)]  # Randomly choose a challenge
    print(z)  # Indicate which challenge was selected (for debugging or testing purposes)

    # Execute the chosen challenge
    if z == "factorial":
        return math_challenge_factorial()
    elif z == "prime":
        return match_challenge_prime()
    else:
        return math_roulette_challenge()


# Main entry point for testing the maths_challenge function
if __name__ == "__main__":
    maths_challenge()
