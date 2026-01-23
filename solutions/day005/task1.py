#50 random integers between 1 and 100, stored in a list called random_numbers    
import random
random_numbers = [random.randint(1, 100) for _ in range(50)]
#now find the max using for loop instead of the simpler max function
max_number = random_numbers[0]  # Assume the first number is the maximum initially
for number in random_numbers:
    if number > max_number:
        max_number = number 
# Output the list and the maximum number
print("The list of random numbers is:", random_numbers)
print("The maximum number in the list is:", max_number) 