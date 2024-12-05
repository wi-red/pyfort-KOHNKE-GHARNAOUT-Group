import random

def factorial(n):

    N = 1
    if n > 0:
        for i in range(0, n):
             N = N*(n - i)

    return(N) 

def math_challenge_factorial():

    n = random.randint(1,10)

    print(f"Math challenger: Calculate the factorial of {n} " )

    X = None
    X_int = False 

    while not X_int:
        try:
            X = int(input("Your answer is: "))
            X_int = True
        except ValueError:
            print("Your answer should be an integer! Please try again.")

    if X == factorial(n):
        return(True)
    else:
        return(False)


if math_challenge_factorial() == True:
    print("Correct ! you win a key.")
else:
    print("Wrong answer... Try again.")