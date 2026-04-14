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
    """
    Creates list of a deck of cards. 

    Returns: 
    - deck: list of remaining cards
    """
    # Define suits and numbers
    # For each suit and for each value: create a card and add it to deck

    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for value in values:
            card = (value, suit)
            deck.append(card)
    
    for card in deck:
        print(f"{card[0]} of {card[1]}") # debugging

    pass

def deal_card(deck):
    """
    Removes and returns one card from the deck.

    Inputs: 
    - deck: list of remaining cards

    Returns:
    - card: the card drawn from the deck
    """
    pass

def calc_score():
    """
    Calculates total value of the hand. 

    Inputs:
    - hand: list of cards

    Returns:
    - int: total score, accounting for ace cards
    """
    pass

def check_blackjack(hand):
    """
    Checks if the player has a natural blackjack.

    Inputs: 
    - hand: list of cards

    Returns: 
    - Bool: True if blackjack, else False
    """
    pass

def display_hand():
    """
    UI to display and print the hand.

    Inputs:
    - hand: list of cards

    Returns:
    - None (prints hand to console)
    """
    pass

def player_turn(deck, hand):
    """
    Handles player's actions during their turn.

    Inputs:
    - deck: list of remaining cards
    - hand: current player hand

    Returns: 
    - hand: final player hand after hitting or standing
    """
    pass

def dealer_turn(deck, hand):
    """
    Logic to decide dealer's action.

    Inputs: 
    - hand: current dealer hand
    - deck: list of remaining cards

    Returns:
    - draws card if score < 17
    - else, stand
    """
    pass

def compare_hands(player, dealer):
    """
    Compare the player's hand to dealer's. 
    
    Inputs: 
    - player: player's hand
    - dealer: dealer's hand

    Returns: 
    win, lose, push
    """
    pass

def play_round(deck, money):
    """ 
    Plays a round of Vegas Strip Blackjack.

    Input: 
    - Money: player's current money

    Returns: 
    - Updates money (int)
    """
    pass

def main():
    pass

if __name__ == "__main__":
    main()

