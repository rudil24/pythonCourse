#rudil24 Python Pizza exercise
print("Welcome to Python Pizza Deliveries!")
#use .upper() to ensure input is raised to uppercase
size = input("What size pizza do you want? S, M, or L: ").upper()    
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else: 
    print("Expected S, M or L.")
    exit()
#get inputs separately to allow for exit on bad input
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
