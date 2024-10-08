# Blackjack Game Project
import random

# Function to deal a random card
def deal_card(): 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.randint(0, len(cards) - 1)
    return cards[index]

# Function to calculate a list of cards
def calculate_score(cards):
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# Function to determine who wins (compare score)
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It' a Draw!"
    elif dealer_score == 0:
        return "You Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You Win with a Blackjack!"
    elif user_score > 21:
        return "You went over, You lose!"
    elif dealer_score > 21:
        return "Opponent went over, You win!"
    elif user_score > dealer_score:
        return "You Win!"    
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # Drawing 2 random card for both user and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if (user_score == 0 or dealer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            user_deal_input = input("Type 'Y' to get another card, type 'N' to pass: ")
            if (user_deal_input.upper() == 'Y'):
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score {dealer_score}")
    print(compare(user_score, dealer_score))

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper() == 'Y':
    print(logo)
    play_game()
    