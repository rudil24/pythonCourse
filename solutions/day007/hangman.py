import random
from hangman_art import logo, stages # Assuming these are in separate files
from hangman_words import word_list # Assuming this is in a separate file

# --- Setup ---
print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6 # Starting lives
display = ["_"] * word_length # Create blanks for each letter
end_of_game = False
guessed_letters = [] # To track already guessed letters

# --- Game Loop ---
while not end_of_game:
    print(f"Current word: {' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    # TODO-4: If the user has entered a letter they've already guessed, print a message
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
    else:
        guessed_letters.append(guess) # Add guess to list

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            # Update the display with the correct letter
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            # If the letter is not in the word, lose a life
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(stages[lives]) # Show the hangman stage

            # Check if user is out of lives (lose condition)
            if lives == 0:
                end_of_game = True
                print(f"You lose! The word was: {chosen_word}")

    # Check if user has won (no more blanks)
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Show current status (win/loss messages handled above, this shows display)
    print(f"{' '.join(display)}")
# end of game