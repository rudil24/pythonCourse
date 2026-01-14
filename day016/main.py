"""
rudil24
Coffee Machine Program (OOP Version)
Refactored to use external classes based on Coffee+Machine+Classes+Documentation.pdf
"""
import time
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# Assuming rutils.py and art.py are in the same directory
from rutils import clear
from art import logo

def main():
    # Instantiate objects from the imported classes
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

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
            print("Welcome to Java Crypt! (OOP Version)")

        # Reset flags to defaults for the next interaction (successful customer flow)
        should_pause = True
        should_clear = True

        # Requirement 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
        options = menu.get_items() 
        choice = input(f"What would you like? ({options}): ").lower()

        # Requirement 2: Turn off the Coffee Machine by entering "off"
        if choice == "off":
            is_on = False
        
        # Requirement 3: Print report
        elif choice == "report":
            # Requirement 3a: Show the current resource values (Water, Milk, Coffee)
            coffee_maker.report() 
            # Requirement 3a/6b: Show Money/Profit in the report
            money_machine.report() 
            
        else:
            # Search the menu for a particular drink by name
            drink = menu.find_drink(choice) 
            
            # Check if find_drink returned a MenuItem or None
            if drink is not None:
                # Requirement 4: Check resources sufficient? (4a, 4b, 4c)
                if coffee_maker.is_resource_sufficient(drink): 
                    # Requirement 5: Process coins (5a, 5b, 5c)
                    # Requirement 6: Check transaction successful? (6a, 6b, 6c)
                    # Note: make_payment handles coin prompting, calculation, and change logic internally.
                    if money_machine.make_payment(drink.cost): 
                        # Requirement 7: Make Coffee (7a, 7b)
                        coffee_maker.make_coffee(drink) 
            else:
                # UX Fix: On invalid selection (menu.find_drink returns None), 
                # do not pause and do not clear screen so user sees error.
                should_pause = False
                should_clear = False

if __name__ == "__main__":
    main()