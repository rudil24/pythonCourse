def calculate_love_score(person1, person2):
    # Combine names and convert to lowercase
    combined_names = (person1 + person2).lower()

    # Count occurrences of letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")

    # Count occurrences of letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Form the love score
    love_score = int(f"{true_count}{love_count}")

    return love_score
# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
love_score = calculate_love_score(name1, name2)
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")   
# End of Love Calculator