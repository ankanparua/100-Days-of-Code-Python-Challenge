import art
print(art.logo)
game = 0
players = {}

def new_bid():
    name = input("What is your name: ")
    bid = input("What is your bid: $")
    players[name] = bid

new_bid()
while game == 0:
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidder == "no":
        game = 1
    elif other_bidder == "yes":
        new_bid()
    else:
        print("Please enter 'yes' or 'no'")
maximum = max(players, key=players.get)
print(f"The winner is {maximum} with a bid of ${players[maximum]}")



