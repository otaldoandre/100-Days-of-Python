from art import *


print(logo)
print("Welcome to the secret auction program.")
bidders = {}
highest_bidder = ""
highest_bid = 0

is_auction_over = False
while not is_auction_over:
    user_name = input("What's your name? ")
    user_bid = input("What's your bid? ")
    bidders[user_name] = user_bid
    
    other_bidders = input("\nAre there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == "yes" or other_bidders == "y":
        continue
    else:
        is_auction_over = True
        for bidder, bid in bidders.items():
            if int(bid) > highest_bid:
                highest_bid = int(bid)
                winner = bidder

print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")

    
    

