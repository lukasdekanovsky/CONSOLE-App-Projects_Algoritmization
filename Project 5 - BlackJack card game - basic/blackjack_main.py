import random
from graphic import logo
import os

#-------------------------------BASIC FUNCTIONS----------------------------------------------
def provide_sum(list_to_make_sum):
    count = 0
    for i in range(len(list_to_make_sum)):
        count += list_to_make_sum[i]
    return count                                    # return sum on int in any list provided as an argument

def initial_deal(number_of_cards, player_cards, computer_cards):
    for i in range(number_of_cards):                          
        player_cards.append(dealing_cards())
        computer_cards.append(dealing_cards())
    return player_cards, computer_cards             # -> return 2 lists player_cards[a, b] , computer_cards[c, d] with cards randomly selected

def dealing_cards():
    cards = [11, 9, 10, 10, 10, 10]
    listed_card = random.choice(cards)
    return listed_card                              # -> return one individual deal

def initialize_game():                              # game initialization with logo and 2 cards for dealer and player
    print(logo)
    player_cards = []
    computer_cards = []
    return initial_deal(2, player_cards, computer_cards)

def next_card(list_of_cards):            
    list_of_cards.append(dealing_cards())
    return list_of_cards                            # dealing next card and appending to the existing list of cards

# ----------------------------------MAIN BLACKJACK LOGIC----------------------------------------------------
def score_and_evaluate_game(player_count, computer_count, player_score, computer_score):
    """Function responsible for evaluation of the score and personal message about who won tha match"""
    if player_count < 21 and computer_count < 21 and computer_count!= player_count:
        if player_count > computer_count:
            player_score += 1
            print("Player Won")
        else:
            computer_score += 1
            print("Computer Won")
    elif player_count == 21 and computer_count != 21:
        player_score += 1
        print("Player Won via BlackJack")
    elif computer_count == 21 and player_count != 21:
        computer_score += 1
        print("Computer Won via BlackJack")
    elif player_count > 21 and computer_count < 21:
        computer_score += 1
        print("Computer Won")
    elif computer_count > 21 and player_count < 21:
        player_score += 1
        print("You Won")
    elif computer_count == player_count:
        print("Draw")
    return player_score, computer_score

def continue_game(player_cards, computer_cards):
    """Function responsible for checking if we can still continue the game. Additionaly we are solving the ace switch from 11 to 1 if score > 21 and still have ace of the value 11"""
    player_count = provide_sum(player_cards)
    computer_count = provide_sum(computer_cards)
    if player_count < 21 and computer_count < 21:
        return True
    elif player_count > 21  and 11 in player_cards :
        player_cards.remove(11)
        player_cards.append(1)
        print(f"# Ace shift 11 -> 1; Your cards: {player_cards} total count: {provide_sum(player_cards)}")
        return True
    elif computer_count > 21  and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
        return True
    elif player_count == 21 or computer_count == 21:
        return False
    else:
        return False                                

def add_another_card(player_cards, computer_cards, game_finish):
    """Function responsible for adding new cards if possible continue in game --> continue(), if so we can decide to continue or cancel the run.
    After player holds, script add aditional cards to the delaer list if < 17.
    Returns: both card lists and game finish bool"""
    possible_to_continue = continue_game(player_cards, computer_cards)
    if possible_to_continue:
        print("--------------------- ANOTHER CARD ? -----------------------------------")
        continue_decision = input("Do you want another card? (y/n): ")
        if continue_decision == "y":
            next_card(player_cards)
            game_finish = False
            return player_cards, computer_cards, game_finish
        elif continue_decision == "n":
            computer_count = provide_sum(computer_cards)
            while computer_count < 17:
                next_card(computer_cards)
                computer_count = provide_sum(computer_cards)
            game_finish = True                                                      # Run stop by decision
            return player_cards, computer_cards, game_finish
    else:
        game_finish = True                                                          # Run stop by continue() function
        return player_cards, computer_cards, game_finish

def run_game(player_cards, computer_cards, player_score, computer_score):
    """Main Game function taking player and computer card sets and looping the add_another_card() function until we recieve game_finish True bool"""
    game_finish = False
    #------------------------------------------------------------------------------------------------------------------------------
    while not game_finish:
        print(f"# Your cards: {player_cards} total count: {provide_sum(player_cards)}")    
        print(f"# Computer card: {computer_cards[0]}") 
        player_cards, computer_cards, game_finish = add_another_card(player_cards, computer_cards, game_finish)
        if game_finish:                                         # if game finish from decision trea of Play() TRUE then evaluate who won
            player_count = provide_sum(player_cards)
            computer_count = provide_sum(computer_cards)
            print("------------------------RESULTS---------------------------------")
            print(f"# Your count     = {player_count}     with cards {player_cards}")           # -> sum of the actual list
            print(f"# Computer count = {computer_count}     with cards {computer_cards}")         # -> sum of the actual list
            score_and_evaluate_game(player_count, computer_count, player_score, computer_score)
    #------------------------------------------------------------------------------------------------------------------------------
    # GAME RESET BOOL --> new game        
    repeat_blackjack_game = input("Do you want to repeat game? (y/n): ")
    if repeat_blackjack_game == "y":
        new_game = False
        os.system("cls")
        return new_game
    else:
        new_game = True
        return new_game

def main():
    new_game = False
    player_score = 0
    computer_score = 0
    while not new_game:
        print("---------------------------------------------------------------------------")
        print(f"TOTAL GAME SCORE || Player: {player_score} VS. Computer: {computer_score}")
        player_cards, computer_cards = initialize_game()
        new_game = run_game(player_cards, computer_cards, player_score, computer_score)
        player_count = provide_sum(player_cards)
        computer_count = provide_sum(computer_cards)
        player_score, computer_score = score_and_evaluate_game(player_count, computer_count, player_score, computer_score)
    print("Thank you for the game!")

if __name__ == "__main__":
    main()