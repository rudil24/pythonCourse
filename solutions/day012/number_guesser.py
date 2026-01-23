# Program a 1 player Game where 
# 1. user first chooses easy or hard version. (EASY number of attempts (10) vs HARD number of attempts (5) (global constants that can be changed). 
# 2. the program asks the user to guess a random number between 1 and 100.
# 3. the program tells the user if their guess is too high or too low.
# 4. then decrements the number of attempts remaining, and tells the user.
# 5. the game ends when the user guesses the number or runs out of attempts.
# 6. "go again?" prompt at the end, to let the user start from step 1.
import random
# Ensure these modules exist in local folder
from art import logo 
from rutils import clear

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # --- Input Validation for Difficulty ---
    attempts_remaining = 0
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            attempts_remaining = EASY_ATTEMPTS
            break
        elif difficulty == 'hard':
            attempts_remaining = HARD_ATTEMPTS
            break
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")
    
    random_number = random.randint(1, 100)
    
    # --- Main Guessing Loop ---
    while attempts_remaining > 0:   
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        
        # Note: This will still crash if they type a non-number (e.g., "ten").
        # We can fix that in the next step if you like.
        guess = int(input("Make a guess: "))
        
        if guess == random_number:
            print(f"Congratulations! You guessed the number {random_number} correctly!")
            return # Exit the function immediately on win
        elif guess < random_number:
            print("Too low.")
        else:
            print("Too high.")
            
        attempts_remaining -= 1
    
    # This only runs if the loop ends normally (attempts == 0)
    print(f"Sorry, you've run out of attempts. The number was {random_number}.")

# --- Main Execution Block ---
while True: #made False when user wants to quit
    clear()
    game()
    
    # Check if user wants to quit
    if input("Do you want to play again? Type 'yes' or 'no': ").lower() != 'yes':
        print("Thanks for playing!")
        print("Goodbye!")
        break