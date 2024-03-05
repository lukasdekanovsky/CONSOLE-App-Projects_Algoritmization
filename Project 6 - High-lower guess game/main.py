from game_data import data
from graphic import logo, vs
import random
import os

def check_correct_answer(account_a, account_b, player_guess):   
    """Function is taking a two dict() accounts and player guess (higher is A r B account) and compare it.
    Function returns False, if the answer is correct to continue the main game loop"""  
    if player_guess == "A" and (account_a['follower_count'] > account_b['follower_count']):
        return False
    elif player_guess == "B" and (account_a['follower_count'] < account_b['follower_count']):
        return False
    elif player_guess != "A" and player_guess != "B":
        print("Wrong typing.")
        return True
    else:
        return True

def generate_account():                     # returns random dict from data list
    """Function generates random dict() from a list of dicts() called and imported as data"""
    return random.choice(data)

def formate_account(account):               # returns tuple from account (name, description, country)
    """Function takes values from dict using the keys such as name, description and state.
    It returns it in the formated way using f string to be directly usable via print()"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    follow = account["follower_count"]
    return f"{name}, a {description}, from {country}"   # ADD follow to see the results

def play_game(game_finish):                 # main play game function
    """Main game logic, until we choose correct answer, our score grows and we can continue.
    After that, we can restart the game typing -> y"""
    # ---------- SCORE ----------------
    score = 0
    # ------- MAIN LOOP BOOL -----------
    wrong_guess = False
    account_switch = False
    # ----------- LOOP -----------------
    while not wrong_guess:
        print(logo)
        if score > 0:
            print(f"You are right! Current score: {score}")        # print from first right answer
        if not account_switch:                                      # account switch is True (correct answer) = this code section is not run 
            account_a = generate_account()
        account_b = generate_account()                              # account_b is randomly chosen each time
        print(f"Compare A:  {formate_account(account_a)}")
        print(vs)
        print(f"Against B:  {formate_account(account_b)}")
        player_guess = input("Who has more followers? Type \"A\" or \"B\": ")
        wrong_guess = check_correct_answer(account_a, account_b, player_guess)
        if not wrong_guess:             # this code section runs if answer was correct
            account_switch = True
            print("Correct")
            os.system("cls")
            account_a = account_b      # account_a is no more random generated if answer was correct, account_b becomes our new account _a
            score += 1
        elif wrong_guess:
            account_switch = False              
    # --------------- RESTART -------------------------
    continue_game = input("Do you want to restart the game? (y/n): ")
    if continue_game == "y":
        game_finish = False
        os.system("cls")
        return game_finish
    elif continue_game == "n":
        game_finish = True
        print("Thank you for the game")
        return game_finish

def main():
    game_finish = False
    while not game_finish:
        game_finish = play_game(game_finish)

if __name__ == "__main__":
    main()