import random

def guess(x):
    radom_number = random.randint(1, x)
    guess = 0
    while guess != radom_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < radom_number:
            print("Sorry! Guess again. Too low")
        elif guess > radom_number:
            print("Sorry! Guess again. Too High")
    print(f"Yay, Congrats! You have guessed the number {radom_number}")

guess(10)
