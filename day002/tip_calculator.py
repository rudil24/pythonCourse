# rudil24: Tip Calculator that calculates the total bill including tip and splits it among a number of people
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? (eg 15, 20, 22.5)) "))
num_people = int(input("How many people to split the bill? "))
tip = (tip_percentage / 100) * bill
total = tip + bill
bill_per_person = total / num_people
print(f"Each person should pay: ${bill_per_person:.2f}")
#.2f in the formatted string ensures that the amount is rounded to 2 decimal places, it's essentially the same as using the round() function.