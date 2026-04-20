import random
import os
import time

def clear():
    """
    Clears the terminal for a clean UI.

    Output:
    - clear 
    """
    # have it clear terminal on both windows and mac
    os.system('cls' if os.name == 'nt' else 'clear')


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

    for _ in range(8): # vegas is 8 deck blackjack
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

def card_format(card):
    """ 
    Formats card to display as "X of Ys".
    ex: Jack of Hearts

    Inputs: 
    card: card in hand

    Returns:
    - formatted card
    """

    # return card[0] of card[1]
    return f"{card[0]} of {card[1]}"

def hand_format(hand):
    """
    Formats hand to display all cards as "X of Ys". 
    ex: Jack of Hearts, Ace of Spades

    Inputs:
    - hand: list of cards

    Returns: 
    - formatted hand
    """
    # return formatted hand by calling card_format 
    return [card_format(card) for card in hand]



def render_card(card, hidden=False):
    """
    Rendering ASCII of cards.

    Inputs:
    - card: card in hand
    - hidden=False: dealer's hidden card 

    Returns:
    - None (prints hand to console)
    """
    
    # match each suit to the symbol
    symbols = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}

    # abbreviate jack, queen, king, ace
    abbreviations = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}

    # if card is hidden (dealer's card), return a special ascii card
    if hidden: 
        return [
            "┌─────────┐",
            "│ ?       │",
            "│         │",
            "│    ?    │",
            "│         │",
            "│       ? │",
            "└─────────┘"
        ]

    # set variable for card's value
    value = card[0]

    # also set variable for abbreviations with .get
    value = abbreviations.get(value, value) # will look for abbrevation value first

    # set variable for turning card's suit into a symbol
    suit = symbols[card[1]]

    # 10 is two characters wide so fix alignment
    if value == "10":
        top = f"│ 10      │"
        bottom = f"│      10 │"
    else: 
        top = f"│ {value:<2}      │" #<2 means left centered
        bottom = f"│      {value:>2} │"  #>2 means right centered

        # else, have the value be left aligned on top and right aligned on bottom


    # return ASCII card
    return [
        "┌─────────┐",
        top,
        "│         │",
        f"│    {suit}    │", #should be 4 spaces on each side (middle)
        "│         │",
        bottom,
        "└─────────┘"
    ]


def render_hand(hand, hide_first=False):
    """
    UI to display and print the hand.

    Inputs:
    - hand: list of cards
    - hide_first = False: hide dealer's second card on player turn

    Returns:
    - None (prints hand to console)
    """
    # make a list of rendered cards
    cards = []
    for mark, card in enumerate(hand):
        if hide_first and mark == 0:
            cards.append(render_card(card, hidden=True))
        else:
            cards.append(render_card(card))
    # use zip to make cards stay on the same row
    # join each row and print
    for row in zip(*cards):
        print("  ".join(row))

def player_turn(deck, hand, dealer_hand):
    """
    Handles player's actions during their turn.

    Inputs:
    - deck: list of remaining cards
    - hand: current player hand
    - dealer_hand: current dealer hand

    Returns: 
    - hand: final player hand after hitting or standing
    """
    # loop while player is playing

    while True:
        # show player their hand
        # show player score
        clear()
        print("Dealer's Hand:")
        render_hand(dealer_hand, hide_first=True)
        print(f"Dealer's Score: ?") 
        print("\nYour Hand:")
        render_hand(hand)
        score = calc_score(hand)
        print("Your Score:", score)

        # check if they bust already
        # if score > 21, bust and break loop

        if score > 21:
            print("You bust.")
            time.sleep(1)
            return hand 
        
        if score == 21:
            print("21! Standing automatically.")
            time.sleep(1)
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
        
        elif action == "quit":
            quit()

        else: 
            print("Invalid input.")


def dealer_turn(deck, hand, player_hand):
    """
    Logic to decide dealer's action.

    Inputs: 
    - hand: current dealer hand
    - deck: list of remaining cards
    - player_hand: current player hand

    Returns:
    - draws card if score < 17
    - else, stand
    """

    while True:
        time.sleep(1) 
        clear()

        score = calc_score(hand)
        print(f"The Dealer reveals: {card_format(hand[0])}")
        print(f"Leading to a score of: {calc_score(hand)}")
        time.sleep(2)

        print("\nDealer's Hand:")
        render_hand(hand)
        print("\nYour Hand:")
        render_hand(player_hand)
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
        return "lose"
    
    # elif dealer > 21, you win, return win

    elif dealer_score > 21:
        return "win"

    # elif player > dealer, you win, return win

    elif player_score > dealer_score:
            return "win"

    # elif player < dealer, you lose, return lose

    elif player_score < dealer_score:
            return "lose"

    # else, it's a tie, return push

    else:
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

    if len(deck) < 52:
        print("Reshuffling...")
        deck.clear()
        deck.extend(create_deck())

    # take bet 
    while True:
        try:
            bet = int(input("Place your bet: "))
            if bet < 15:
                print("Minimum bet is $15.")
            elif bet > 100:
                print("Maximum bet is $100.")
            elif bet > money:
                print(f"You only have ${money}.")
            else:
                break
        except ValueError:
            print("Please enter a number.")


    # create deck
    # deal cards 
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("\nThe Dealer has:", card_format(dealer_hand[0])) # only reveals his first card)

    if check_blackjack(player_hand):
        print("Blackjack!")
        money += int(bet * 1.5) # 3:2 payout for nat blackjack in Vegas
        return money

    # player turn
    player_hand = player_turn(deck, player_hand, dealer_hand)


    if calc_score(player_hand) > 21:
        clear()
        print("Dealer's Hand:")
        render_hand(dealer_hand)
        print("\nYour Hand:")
        render_hand(player_hand)
        print("\nYou busted. Round over.")
        money -= bet
        time.sleep(4)
        return money

    # dealer turn

    dealer_hand = dealer_turn(deck, dealer_hand, player_hand)

    # compare hands

    result = compare_hands(player_hand, dealer_hand)

    clear() 
    print("Dealer's Hand:")
    render_hand(dealer_hand)
    print(f"Dealer's Score: {calc_score(dealer_hand)}")
    print("\nYour Hand:")
    render_hand(player_hand)
    print(f"Your Score: {calc_score(player_hand)}")

    if result == "win":
        money += bet
        print("\nYou win the round.")
    elif result == "lose":
        money -= bet
        print("\nYou lose the round.")
    else:
        print("\nPush. It's a tie.")


    time.sleep(4)
    return money



def main():


    deck = create_deck()
    money = 500

    while 0 < money < 1500:
        money = play_round(deck, money)

    print("Game over. Final money:", money)



if __name__ == "__main__":
    main()