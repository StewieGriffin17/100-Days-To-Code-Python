# Blind auction project
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to silent auction. Just insert your name and bid. Winner will be declared after everybody place a bid.\n")

bidders = {}
anybody_left = True


def highest_bidder(bidders_info):
    highest = 0
    winner = ""
    for bidder in bidders_info:
        bid_amount = bidders_info[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with ${highest} bid.")


while anybody_left:
    name = input("What's your name? ")
    bid = int(input("How much do you want to bid? "))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or no. ").lower()
    if should_continue == 'yes':
        print('\n' * 100)
    elif should_continue == 'no':
        highest_bidder(bidders)
        anybody_left = False
