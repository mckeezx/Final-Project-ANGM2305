# Game Loop 
# Player starts with $100 
# If money is more than $0 and less than $300 play a round (Core)
# Update money after round
# When it ends, show win or lose

# Core Loop (round)
# Betting
# Deal Cards
# Check for Blackjack
# Player Turn
# Dealer Turn
# Compare Results
# Update Money

# Player Loop 
# While player is still playing:
# show hand
# ask what they want to do
# Hit to add card
# Stand to exit loop
# Check if they bust then end turn

# Dealer Logic
# While dealer cards are less than 17:
# draw a card

# Compare Results
# If player busts then lose
# ELIF dealer busts then win
# ELIF player > dealer then win
# ELIF player < dealer then lsoe
# ELSE push/tie

def create_deck():
    pass

def deal_card():
    pass

def calc_score():
    pass

def check_blackjack(hand):
    pass

def display_hand():
    pass

def player_turn(deck, hand):
    pass

def dealer_turn(deck, hand):
    pass

def compare_hands(player, dealer):
    pass

def play_round(deck, money):
    pass

def main():
    pass

if __name__ == "__main__":
    main()

