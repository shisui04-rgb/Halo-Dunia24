import random

def guess_the_number():
    """Guess the Number game."""
    number_to_guess = random.randint(1, 100)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f" Congratulations! You guessed the number: {number_to_guess}")
            break

guess_the_number()
