# ---------------------------- GLOBAL VARIABLE -------------------------------------s
profit = 0
# --------------------------------------------------------------------------------------------
def refill_resources(start_resources, resources):
    """Function used to refill all resources to max value"""
    for key in resources:
        resources[key] = start_resources[key]

def see_machine_resources(resources):
    """Function pronts all remaining resources and all money gained from customers"""
    print(f"Water:  {resources['water']}  ml")
    print(f"Milk:   {resources['milk']}  ml")
    print(f"Coffee: {resources['coffee']}  g")
    print(f"Money:  {profit}$")

def decrese_resources(choice, menu, resources):
    """Function removes adequate resources from machine once called, reflecting resources needed from recipe"""
    consumed_resources = menu[choice]["ingredients"]
    for key in consumed_resources:
        resources[key] -= consumed_resources[key]

def insert_coins(): 
    """Function for coins insertion, returns total amount of money inserted"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) # 0.25 $
    dimes = int(input("How many dimes?: "))       # 0.1  $
    nickles = int(input("How many nickles?: "))   # 0.05 $
    pennies = int(input("How many pennies?: "))   # 0.01 $
    money_inserted = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01* pennies
    return money_inserted

def check_money(money_inserted, choice, menu):
    """Function check if enought money inserted and returns whats above, item price is added to profit variable"""
    global profit                           # we need to access global variable profit
    money_required = menu[choice]["cost"]
    if money_required <= money_inserted:    # if there is enought money inserted
        profit += money_required
        money_back = money_inserted-money_required
        print(f"Money back: {round(money_back, 2)}$ in change.")
        return True
    else:
        return False

def check_resources(choice, menu, resources):
    """Function controls if we have enought resources in machine to provide coffee"""
    required_recipe = menu[choice]["ingredients"] 
    for key in required_recipe: 
        if resources[key] < required_recipe[key]:
            print("Not enought resources - refill machine and type (reset)")
            return False
        else:
            pass                            # This function returns FALSE only if the script will find that there is not enought resources in one or more items
    return True

def run_coffee_machine(stop_machine, menu, start_resources, resources):
    """Main coffee machine function, running the whole machine"""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":                     # turn off the machine
        stop_machine = True
        return stop_machine
    elif choice == "report":                # ask for all ingredients
        see_machine_resources(resources)
    elif choice == "reset":                 # reset the resources after refilling 
        refill_resources(start_resources, resources)
    elif choice in menu.keys():
        if check_resources(choice, menu, resources):                         # will pass only with enought resources
            money_inserted = insert_coins()
            if check_money(money_inserted, choice, menu):         # will pass only if we inserted enought money
                decrese_resources(choice, menu, resources)
                print(f"Here is your {choice} . . . Enjoy :) :)")
            else:
                print("Not enought money inserted. Money refunded.")
    else:
        print("Please write again your order.")

def main():
    menu = {
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
    start_resources = {
    "water": 5000,
    "milk": 3000,
    "coffee": 2000,
}
    resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
}
    stop_machine = False
    while not stop_machine:
        stop_machine = run_coffee_machine(stop_machine, menu, start_resources, resources)

if __name__ == "__main__":
    main()