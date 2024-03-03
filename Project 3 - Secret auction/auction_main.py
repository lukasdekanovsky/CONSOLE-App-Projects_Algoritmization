import os 
from graphic import logo


def ask_for_bids(individual_competitor):        # code responsible for collecting the bids and returnign individual competitors in the form of dictionary
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    individual_competitor[name] = bid
    return individual_competitor 

def evaluate_highest_bid(auction_competitors):  # code responsible for selection of the highest offer from a dictionary values
    best_bid = 0
    winner = ""
    for individual in auction_competitors:
        if auction_competitors[individual] > best_bid:
            best_bid = auction_competitors[individual]
            winner = individual
    print("---------------------------------------------------------------------------------------")
    print(f"Winner of the secret auction is becomming: {winner} for the bid of: {best_bid} $")
    print("---------------------------------------------------------------------------------------")
    #print(f"Auction competitors: {auction_competitors}")

def main():
    print(logo)
    print("Welcome to the secret auction program.")
    auction_competitors = {}
    last_bid = False
    while not last_bid:
        ask_for_bids(auction_competitors)
        another_bids = input("Are there any other bidders? Type \"yes\" or \"no\".\n")
        #print(auction_competitors)
        if another_bids == "yes":
            os.system("cls")
        else:
            last_bid = True
            evaluate_highest_bid(auction_competitors)
    
if __name__ == "__main__":
    main()

