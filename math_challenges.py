import random

#----------------FACTORIAL GAME----------------#
def factorial(n):

    N = 1
    if n > 0:
        for i in range(0, n):
             N = N*(n - i)

    return(N) 

def math_challenge_factorial():
    print("\n#----------------FACTORIAL GAME----------------#\n")
    print("Welcome to the Factorial Game!")
    n = random.randint(1,10)

    print(f"\nMath challenger: Calculate the factorial of {n}.\n" )

    X = None
    X_int = False 

    while not X_int:
        try:
            X = int(input("Your answer is: "))
            print(" ")
            X_int = True
        except ValueError:
            print("Your answer should be an integer! Please try again.")

    if X == factorial(n):
        return("Correct answer! you've won a key.\n")
    else:
        return("Wrong answer... Better luck next time.\n")



#----------------PRIME GAME----------------#

def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return False
    else:
        return True
#print(is_prime(21))

def nearest_prime(n):
    c=n+1
    while not is_prime(c):
        c+=1
    return c

def match_challenge_prime():
    print("\n#----------------PRIME GAME----------------#\n")
    print("Welcome to the Prime Game!")
    N=random.randint(10,20)
    X_int = False
    print(f"\nMath Challenge: Find the nearest prime to {N}.\n")
    while not X_int:
        try:
            X=int(input("Your answer is : "))
            print(" ")
            if X==nearest_prime(N):
                return("Correct answer! You've won a key.\n")
            else:
                return("Wrong answer... Better luck next time!\n")
        except ValueError:
            print("\nYour value should be an integer ! Please try again.")

#----------------MATH ROULETTE GAME----------------#
def math_roulette_challenge():
    print("\n#----------------MATH ROULETTE GAME----------------#\n")
    L1=['*','+','-']
    L2=[]
    X_int=False
    print("Welcome to the Roulette Game!")
    for i in range(5):
        L2.append(random.randint(1,20))
    op=L1[random.randint(0,2)]
    if op=="*":
        print("\nCalculate the result by combining these numbers with multiplication\n")
        result=L2[0]
        for i in range(1,5):
            result*= L2[i]
    elif op=='+':
        result=L2[0]
        print("Calculate the result by combining these numbers with addition\n")
        for i in range(1,5):
            result+= L2[i]
    elif op == '-':
        result=L2[0]
        print("Calculate the result by combining these numbers with subtraction\n")
        for i in range(1,5):
            result -= L2[i]
    print("|TESTING ONLY| ANSWER IS:",result)
    print("Numbers on the roulette:",L2,"\n")
    while not X_int:
        try:
            X=int(input("Your answer is: "))
            print(" ")
            if X==result:
                return("Correct answer! You've won a key\n")
            else:
                return("Wrong answer... Better luck next time!\n")
        except ValueError:
            print("\nYour value should be an integer ! Please try again.\n")


def maths_challenge():
    challenges=["factorial","prime","roulette"]
    z=challenges[random.randint(0,2)]
    print(z)
    if z == "factorial":
        return print(math_challenge_factorial())
    elif z == "prime":
        return print(match_challenge_prime())
    else:
        return print(math_roulette_challenge())
    

if __name__ == "__main__" :
    maths_challenge()

#WORK LEFT: COMMENTING THE FUNCTIONS