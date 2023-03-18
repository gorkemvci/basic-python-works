import arts , os
print(arts.logobids)
bids={}
def all_bids():
    name_bid = input("What is your name:\n")
    money_bid = int(input("What is your bid:\n$"))
    bids[name_bid] = money_bid
    if input("Is there a new bid? yes or no:\n") == "yes":
        os.system("cls")
        all_bids()
    else:
        os.system("cls")
        print("The bids are End!")    
        
def winner_bid():
    winner_bid_money = 0
    winner_bid_name = "Museum_Art"
    for winner in bids:
        if winner_bid_money < bids[winner]:
            winner_bid_money = bids[winner]
            winner_bid_name = winner
    return f"Winner name is {winner_bid_name}. The with ${winner_bid_money}"

print("Welcome to Public Auction ")
all_bids()
print(winner_bid())