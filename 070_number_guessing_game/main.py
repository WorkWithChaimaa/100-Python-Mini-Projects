# Project 70: Number Guessing Game

import random
secret_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    tries += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {tries} tries")