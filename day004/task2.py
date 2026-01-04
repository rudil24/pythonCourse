# User gives a state abbreviation (e.g., "CA" for California)
# Program tells the user the full name of the state and the order it was admitted to the union
# e.g., "California was the 31st state admitted to the union."

# Dictionary of state abbreviations and full names
state_dict = {'AL' : 'Alabama', 'AK' : 'Alaska', 'AZ' : 'Arizona', 'AR' : 'Arkansas', 'CA' : 'California','CO' : 'Colorado', 'CT' : 'Connecticut','DE' : 'Delaware','FL' : 'Florida','GA' : 'Georgia','HI' : 'Hawaii','ID' : 'Idaho','IL' : 'Illinois','IN' : 'Indiana','IA' : 'Iowa','KS' : 'Kansas','KY' : 'Kentucky','LA' : 'Louisiana','ME' : 'Maine','MD' : 'Maryland','MA' : 'Massachusetts','MI' : 'Michigan','MN' : 'Minnesota','MS' : 'Mississippi','MO' : 'Missouri','MT' : 'Montana','NE' : 'Nebraska','NV' : 'Nevada','NH' : 'New Hampshire','NJ' : 'New Jersey','NM' : 'New Mexico','NY' : 'New York','NC' : 'North Carolina','ND' : 'North Dakota','OH' : 'Ohio','OK' : 'Oklahoma','OR' : 'Oregon','PA' : 'Pennsylvania','RI' : 'Rhode Island','SC' : 'South Carolina','SD' : 'South Dakota','TN' : 'Tennessee','TX' : 'Texas','UT' : 'Utah','VT' : 'Vermont','VA' : 'Virginia','WA' : 'Washington','WV' : 'West Virginia','WI' : 'Wisconsin','WY' : 'Wyoming','DC' : 'District of Columbia'}

# List of states in the order they joined the union
state_list = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# Ask the user for input and provide a prompt that explains we need a state abbreviation 
# Make sure the user input is assigned to a variable, clean it by forcing uppercase
state_input = input("Give me a state abbreviation: ").upper()

# Check if the abbreviation is in the state_dictionary
# If it is not in the state dictionary, give an error message of your choosing and exit()
# if not state_dict.has_key(state_input): #deprecated in Python 3
if state_input not in state_dict:  #the proper way to do it in Python 3
	print("Error: State abbreviation not found. Please use an official USPS 2-letter state abbreviation.")
	exit()
print("good job that is a state")
# Look up the abbreviation in the state_dictionary to get the full name
# Make sure full name is assigned to a variable
state_name = state_dict[state_input]
# Find the index of the item in the list
# Because index will start counting at zero, we want to add 1 to the index to get its order of admission
order = state_list.index(state_name)
order = order + 1
# Format the order as a string
order = str(order)
# extra credit: (hint treat the string like a list)
# if it ends in a "2" add "nd" at the end of the string
# else if it ends in a "1" add "st" at the end of the string
# else if it ends in a "3" add "rd" at the end of the string
# else, add a "th" to the end of the string

# Print the full name of the state and order that it was accepted into the union
#print_statement = "Your state is " + state_name + " the order is " + order
if order.endswith("1") and not order.endswith("11"):
    order += "st"
elif order.endswith("2") and not order.endswith("12"):
    order += "nd"
elif order.endswith("3") and not order.endswith("13"):
    order += "rd"
else:
    order += "th"
print_statement = f"Your state is {state_name}, the {order} state admitted to the union."
print(print_statement)
# End of program