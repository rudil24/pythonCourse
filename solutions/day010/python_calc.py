from rutils import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# --- NEW HELPER FUNCTION ---
def get_valid_number(prompt):
  """
  Repeatedly asks the user for input until a valid number is entered.
  """
  while True:
    user_input = input(prompt)
    try:
      # Try to convert the input to a float
      return float(user_input)
    except ValueError:
      # If it fails, print an error and the loop continues
      print("That's not a valid number. Please try again.")

def calculator():
  print(logo)

  # Use the helper function here
  num1 = get_valid_number("What is the first number?: ")
  
  for symbol in operations:
    print(symbol)
    
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    
    # Use the helper function here as well
    num2 = get_valid_number("What's the next number?: ")
    
    if operation_symbol in operations:
        calculation_function = operations[operation_symbol]
        # Safety check for dividing by zero
        if operation_symbol == "/" and num2 == 0:
             print("Error: Cannot divide by zero.")
             # We don't exit, we just let them try a new calculation or loop
             continue 

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    else:
        print("Invalid operation.")
        return True 

    continue_calc = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit.: ")
    
    if continue_calc == 'y':
      num1 = answer
    elif continue_calc == 'n':
      should_continue = False
      clear()
      return False 
    elif continue_calc == 'q':
      return True
    else: 
      print("Invalid input, exiting.")
      return True

# --- Main Execution ---
exit_program = False

while not exit_program:
  exit_program = calculator()