"""
Plays a game of guess the number with user.
"""

import random

def main():
    """Inputs the bounds of the range of numbers and lets the user guess
    the computer's number until the guess is correct."""
    smaller = int(input("Enter the lower bound: "))
    larger = int(input("Enter the upper bound: "))
    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too large")
        else:
            print("You've got it in", str(count), "tries!")
            break

if __name__ == "__main__":
    main()
