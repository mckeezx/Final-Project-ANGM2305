import random


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
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    for suit in suits:
        for value in values:
            card = (value, suit)
            deck.append(card)
    
    return deck


def deal_card(deck):
    """
    Removes and returns one card from the deck.

    Inputs: 
    - deck: list of remaining cards

    Returns:
    - card: the card drawn from the deck
    """
    # take random card from deck
    # remove it from deck
    # return it 

    card = random.choice(deck)
    deck.remove(card)
    return card


def calc_score(hand):
    """
    Calculates total value of the hand. 

    Inputs:
    - hand: list of cards

    Returns:
    - int: total score, accounting for ace cards
    """
    # create and set score to 0 
    # create and set ace count to 0 (have to account for aces and their score)
    score = 0
    ace = 0

    # for each card in your hand, get the card's value
    for card in hand:
        value = card[0]


        # elif it's a jack, queen, king, add 10 to the score
        if value in ["Jack", "Queen", "King"]:
            score += 10
    
        # elif it's an ace, add 11 to the score and 1 to the ace count
        elif value == "Ace":
            score += 11
            ace += 1
        
        # else if it's a number card just add the integer value to score
        else:
            score += int(value)


    # while score is greater than 21 and ace count more than 0 
    # subtract 10 from score and 1 from ace count
    while score > 21 and ace > 0:
        score -= 10
        ace -= 1

    # return score
    return score

def check_blackjack(hand):
    """
    Checks if the player has a natural blackjack.

    Inputs: 
    - hand: list of cards

    Returns: 
    - Bool: True if blackjack, else False
    """
    # If hand size is 2, check for a blackjack
    # check hand for Ace and a 10 value card (10, Jack, Queen, King)
    # If both exist, return True, else return False
    # Use any to see if any cards in the list are 10, J, Q, K

    if len(hand) != 2:
        return False

    values = [card[0] for card in hand]

    if "Ace" in values and any(card_value in values for card_value in ["10", "Jack", "Queen", "King"]):
        return True
    return False

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
    # loop while player is playing

    while True:
        # show player their hand
        # show player score

        print("\nYour Hand:", hand)
        score = calc_score(hand)
        print("Your Score:", score)

        # check if they bust already
        # if score > 21, bust and break loop

        if score > 21:
            print("You bust.")
            return hand 

        # ask them to hit or stand
        
        action = input("What do you do? ").lower()

        # if hit, deal a card

        if action == "hit":
            print("You draw a card.")
            hand.append(deal_card(deck))

        # if stand, end turn and break loop
        elif action == "stand":
            print("You stand.")
            return hand

        else: 
            print("Invalid input.")


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

    while True:
        score = calc_score(hand)

        print("\nDealer's Hand:", hand)
        print("Dealer's Score:", score)

        # if score is more than 21, bust

        if score > 21:
            print("The Dealer busts.")
            return hand
        
        # if score is more than 17, stand
        elif score >= 17:
            print("The Dealer stands.")
            return hand
        
        # else, hit and draw a card
        else:
            print("The Dealer hits.")
            hand.append(deal_card(deck))


def compare_hands(player_hand, dealer_hand):
    """
    Compare the player's hand to dealer's. 
    
    Inputs: 
    - player: player's hand
    - dealer: dealer's hand

    Returns: 
    win, lose, push
    """

    # if dealer or player busts, we already know, but that just stops their turn
    # calculate dealer and player score

    player_score = calc_score(player_hand)
    dealer_score = calc_score(dealer_hand)


    # if player > 21, you lose, return lose

    if player_score > 21: 
        print("You bust. You lose.")
        return "lose"
    
    # elif dealer > 21, you win, return win

    elif dealer_score > 21:
        print("Dealer busts. You win.")
        return "win"

    # elif player > dealer, you win, return win

    elif player_score > dealer_score:
            print("You win.")
            return "win"

    # elif player < dealer, you lose, return lose

    elif player_score < dealer_score:
            print("You lose.")
            return "lose"

    # else, it's a tie, return push

    else:
        print("Push. (It's a tie).")
        return "push"


def play_round(deck, money):
    """ 
    Plays a round of Vegas Strip Blackjack.

    Input: 
    - Money: player's current money

    Returns: 
    - Updates money (int)
    """

    print("· ♤ · ♡ · New Round · ♢ · ♧ ·")
    print("Current money:", money)

    # take bet 
    bet = int(input("Place your bet: "))

    # create deck
    # deal cards 
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("\nThe Dealer has:", dealer_hand[0]) # only reveals his first card)

    # player turn
    player_hand = player_turn(deck, player_hand)

    # dealer turn

    dealer_hand = dealer_turn(deck, dealer_hand)

    # compare hands

    result = compare_hands(player_hand, dealer_hand)

    # update money
    if result == "win":
        money += bet
    elif result == "lose":
        money -= bet
        
    return money



def main():


    deck = create_deck()
    money = 100

    while 0 < money < 300:
        money = play_round(deck, money)

    print("Game over. Final money:", money)



    # Create hands
    player_hand = []
    dealer_hand = []

    # Deal player 2 cards
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))

    # Deal dealer 2 cards
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    
    # It has been 30 games and I haven't won once. The dealer has gacha levels of RNG.


if __name__ == "__main__":
    main()

