import random

# ASCII Art for Rock, Paper, and Scissors (optional, but a common addition for Day 4)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

(rock)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

(paper)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

(scissors)
'''

# User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Computer choice
computer_choice = random.randint(0, 2)

# ASCII Art for user and computer choices (optional, but a common addition for Day 4)
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("You typed an invalid number! ")


if computer_choice == 0:
    print("Computer chose:")
    print(rock)
elif computer_choice == 1:
    print("Computer chose:")
    print(paper)
else:
    print("Computer chose:")
    print(scissors)

# Game logic
if user_choice >= 3 or user_choice < 0:
    print("You lose!") #we already told them it's invalid above, so now we just inform them they lose
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
