"""
rudil24
Coffee Machine Program
Based on requirements from Coffee Machine Program Requirements.pdf
"""
import time
# Assuming rutils.py and art.py are in the same directory
from rutils import clear
from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 2500,
    "milk": 1000,
    "coffee": 250,
}

profit = 0


def get_valid_integer(prompt_text):
    """Helper to ensure user enters a valid integer for coins."""
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made, False if ingredients are insufficient."""
    # Requirement 4a: Check if there are enough resources to make the drink
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            # Requirement 4b: Print 'Sorry there is not enough [resource].'
            print(f"Sorry there is not enough {item}.") 
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    # Requirement 5a: Prompt user to insert coins
    print("Please insert coins.") 
    
    # Requirement 5b: Remember that quarters=0.25, dimes=0.10, nickles=0.05, pennies=0.01
    quarters = get_valid_integer("how many quarters?: ")
    dimes = get_valid_integer("how many dimes?: ")
    nickles = get_valid_integer("how many nickles?: ")
    pennies = get_valid_integer("how many pennies?: ")

    # Requirement 5c: Calculate the monetary value of the coins inserted
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if the payment is accepted, or False if money is insufficient."""
    # Requirement 6a: Check that the user has inserted enough money
    if money_received >= drink_cost:
        # Requirement 6c: If user inserted too much money, offer change
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        
        # Requirement 6b: Add cost of drink to profit
        global profit
        profit += drink_cost
        return True
    else:
        # Requirement 6a (cont): Refund money if insufficient
        print("Sorry that's not enough money. Money refunded.") 
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    # Requirement 7a: Deduct ingredients from coffee machine resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    
    # Requirement 7b: Tell the user "Here is your [drink]. Enjoy!"
    print(f"Here is your {drink_name}. Enjoy!") 


def main():
    is_on = True 
    
    # Logic flags to control UX flow
    should_pause = False  # Start False to avoid delay on startup
    should_clear = True   # Start True to show logo on startup

    while is_on:
        # UX Enhancement: Logic to handle pauses and screen clearing
        if should_pause:
            time.sleep(10)
            
        if should_clear:
            clear()
            print(logo)
            print("Welcome to Java Crypt!")

        # Reset flags to defaults for the next interaction (successful customer flow)
        should_pause = True
        should_clear = True

        # Requirement 1: Prompt user by asking "What would you like?"
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Requirement 2: Turn off the Coffee Machine by entering "off"
        if choice == "off":
            is_on = False
        
        # Requirement 3: Print report
        elif choice == "report":
            # Requirement 3a: Show the current resource values
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit:.2f}") 
            
        else:
            if choice in MENU:
                drink = MENU[choice]
                # Requirement 4: Check resources sufficient?
                if is_resource_sufficient(drink["ingredients"]):
                    # Requirement 5: Process coins
                    payment = process_coins()
                    # Requirement 6: Check transaction successful?
                    if is_transaction_successful(payment, drink["cost"]):
                        # Requirement 7: Make Coffee
                        make_coffee(choice, drink["ingredients"])
            else:
                print("Invalid selection. Please try again.")
                # UX Fix: On invalid selection, do not pause and do not clear screen
                # This allows the user to see the error message and re-type immediately
                should_pause = False
                should_clear = False

if __name__ == "__main__":
    main()