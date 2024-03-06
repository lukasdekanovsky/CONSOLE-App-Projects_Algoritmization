from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# ------------------ MAIN LOGIC ------------------------------

# 1) object creation:
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

# 2) logic of the machine:
while is_on:
    options = menu.get_items()                          # object "menu" is calling method of it´s instance .get_items() -> return of this method we save in new variable
    choice = input(f"What would you like?: {options}")  # user input 
    # ----- DECISION TREE ----------------------------
    if choice == "off":                                         
        is_on = False
    elif choice == "report":
        coffee_maker.report()   # prints a report of all resources
        money_machine.report()  # prints a report of money
    else:
        order = menu.find_drink(choice)      # returns MenuItem obeject
                                                                                    # MenuItem attribute .cost -> returns the cost            
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
