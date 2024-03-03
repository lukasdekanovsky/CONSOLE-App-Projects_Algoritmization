from graphic import logo
import os

def sum(x, y):
    return x + y

def multiple(x, y):
    return x * y

def devide(x, y):
    return x / y

def minus(x, y):
    return x - y

def round_result(result, how_many_decimals):
    """Takes number and apply round function with passed number of decimals"""
    return round(result, how_many_decimals)

def calculate(x, y, function, round_to):
    """Function sends numbers x and y to the correct function and round the result"""
    return round_result(function(x, y), round_to)

def print_result(result, x, y, operation_select):
    """Function for result printing"""
    print(f"Resuls of {x} {operation_select} {y} = {result}.")

def calculator(operators, x):
    """Function collecting inputs from user and sends them to calculate function --> returning number as a result"""
    #----------------------INPUTS-----------------------------------------------
    if x == 0:
        x = float(input("Number x = ").replace(",", "."))       # number x
    else:
        print(f"Number x = {x}")
    for symbol in operators:                                    # operation selection
        print(symbol)
    operation_select = input("Type operation: ")
    y = float(input("Number y = ").replace(",", "."))           # number y
    round_to = int(input("Result with how many decimals?: "))
    #----------------------RESULTS-----------------------------------------------
    result = calculate(x, y, operators[operation_select], round_to)
    print_result(result, x, y, operation_select)
    return result

def main():
    print(logo)
    operators = {"+": sum, "-": minus, "*": multiple, "/": devide}
    stop_calc = False
    x = 0
    while not stop_calc:
        middle_result = calculator(operators, x)
        what_to_do_next = input("Do you want to continue with this number? (y/n) :")
        if what_to_do_next == "y":
            x = middle_result
        elif what_to_do_next == "n":
            x = 0
            os.system("cls")
            print(logo)
        else:
            print("You tiped wrong letter")
    stop_calc = False
    



if __name__ == "__main__":
    main()