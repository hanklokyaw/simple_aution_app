from art import logo
import os

print(logo)
bid_game = {}
terminate = False


def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} and the bid amount is {highest_bid}")


while not terminate:
    name = input("what is your name?")
    bid_price = int(input("what is your bid price? $"))
    bid_game[name] = bid_price
    if input("Is there another bidder? (yes or no):").lower() == "no":
        terminate = True
        print(bid_game)
        highest_bidder(bid_game)
    else:
        os.system("clear")
        terminate = False
