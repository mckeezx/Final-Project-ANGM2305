import tkinter as tk
from project import create_deck, deal_card, calc_score, check_blackjack, compare_hands, render_card
# this is the GUI of the project, while project.py is the brain

# window set up
# tk.Tk()
window = tk.Tk() #creates window
# 960x540
window.geometry("960x540")
# black bkg
window.configure(bg="black")

# Game state
# create deck
deck = create_deck()
# player hand and dealer hand create list
player_hand = []
dealer_hand = []
# money is 500
money = 500
# bet curerntly at 0
bet = 0

def update_display(text):
    """
    Enables window to be written in, writes text, then disables it again.

    Input:
    - Text: text needed to be written
    
    Output:
    - text written to window
    """
    #set display state to normal
    display.config(state="normal")
    #clear screen
    display.delete("1.0", "end")
    #write text
    display.insert("end", text)
    #set display state to disabled
    display.config(state="disabled")

def draw_board_string(hide_dealer=False):
    """
    Render cards, show player/dealer hand, show money, your bet, score

    Input:    
    - See if dealer's card is hidden or not
    Output:
    - Render stuff to window
    """
    # variables to read: render_card, dealer_hand, player_hand, calc_score, money, bet
    # create empty board string
    board = ""
    # add Dealer's hand
    board += "Dealer's hand:\n"
    for row in zip(*[render_card(c, hidden=(i==0)) for i, c in enumerate(dealer_hand)]):
        board += "  ".join(row) + "\n"
        # do same for player's hand
    board += "\nYour Hand:\n"
    for row in zip(*[render_card(c) for c in player_hand]):
        board += "  ".join(row) + "\n"
        # show score, money, bet
    board += f"\nYour Score: {calc_score(player_hand)}"
    board += f"\nMoney: ${money}  |  Bet: ${bet}"
    # update display
    return board

def draw_board():
    update_display(draw_board_string(hide_dealer=True))

def new_round():
    """
    Plays a new round of blackjack.
    
    
    """
    global player_hand, dealer_hand, bet # global modifies variable outside function

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    draw_board()

def place_bet():
    """
    Tries to take what player typed and read it as an integer.
    
    Output:
    - player bet
    """
    global bet
    try:
        bet = int(bet_input.get())
        if bet < 15:
            update_display("Minimum bet is $15.")
        elif bet > 100:
            update_display("Maximum bet is $100.")
        elif bet > money:
            update_display(f"You only have ${money}.")
        else:
            new_round()
            enable_buttons()
    except ValueError:
        update_display("Please enter a number.")

def disable_buttons():
    """
    Disables buttons from being pressed.
    """
    # set hit/stand/surrender button state to disable
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")
    surrender_button.config(state="disabled")
    

def enable_buttons():
    """
    Enables buttons from being pressed.
    """
    # set hit/stand/surrender button state to normal
    hit_button.config(state="normal")
    stand_button.config(state="normal")
    surrender_button.config(state="normal")

def hit():
    """
    Player can draw a card
    
    Output:
    - add card to player hand
    """
    global player_hand
    player_hand.append(deal_card(deck))
    draw_board()

    # bust checking
    # calc score > 21
    if calc_score(player_hand) > 21:
        # update display saying u bust
        update_display("You bust! Round over.")
        # disable buttons
        disable_buttons()

    # else if == 21, stand automatically
    elif calc_score(player_hand) == 21:
        update_display("21! Standing Automatically.")
        # disable buttons
        disable_buttons()

def surrender():
    """
    Player can surrender, getting half their money back

    Output:
    - Money bet on round divided by 2
    
    """
    global money, bet
    money -= bet // 2
    update_display(f"You surrendered. You keep ${bet // 2}.\nMoney: ${money}")

def stand():
    """
    Player can stand, ending their turn
    
    Output:
    - Stand
    """
    global dealer_hand, money, bet
    # while dealer is less than 17, draw card
    while calc_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    draw_board()

    # compare hands 
    result = compare_hands(player_hand, dealer_hand)
    #if win, win
    if result == "win":
        money += bet
        update_display(draw_board_string() + f"\nYou win! +${bet}  |  Money: ${money}")
    elif result == "lose":
        money -= bet
        update_display(draw_board_string() + f"\nYou lose. -${bet}  |  Money: ${money}")
    #lose, lose
    # else it's tie
    else: 
        update_display(draw_board_string() + f"\nPush. You keep ${bet}  |  Money: ${money}")
    # disable the buttons
    disable_buttons()


#display set up 
display = tk.Text(
    window,
    # bkg black
    bg = "black",
    # fg green
    fg = "green",
    # courier font
    font = ("Courier", 12),
    # disabled state so no typing
    state = "disabled",
    width = 80,
    height = 25
)
# display pack pady=10
display.pack(pady=10) # 10 pixel padding top and bottom

#button set up
# tk.Frame, same bg
button_frame = tk.Frame(window, bg="black")
# pack frame into block
button_frame.pack()
# hit button 
hit_button = tk.Button(button_frame, text="Hit", width=10, bg="gray", fg="white", command=hit)
# stand button
stand_button = tk.Button(button_frame, text="Stand", width=10, bg="gray", fg="white", command=stand)
# surrender button
surrender_button = tk.Button(button_frame, text="Surrender", width=10, bg="gray", fg="white", command=surrender)
# all buttons will be their own frame with white text gray bg 
# use grid format to format them
hit_button.grid(row=0, column=0, padx=5)
stand_button.grid(row=0, column=1, padx=5)
surrender_button.grid(row=0, column=2, padx=5)

# bet input time
# black bg frame
bet_frame = tk.Frame(window, bg="black")
# pack it
bet_frame.pack()

# bet label black bg green fg courier font 
bet_label = tk.Label(bet_frame, text="Bet: $", bg="black", fg="green", font=("Courier", 12))
# it jsuts says "bet", nothing else
# 0,0
bet_label.grid(row=0, column=0)

# bet input same stats kinda
bet_input = tk.Entry(bet_frame, width=10, bg="gray", fg="white", font=("Courier", 12))
# one column down, padx5
bet_input.grid(row=0, column=1, padx=5)
# can take the code with bet_input.get()

# deal button some stats
deal_button = tk.Button(bet_frame, text="Deal", width=10, bg="gray", fg="white", command=place_bet)
# column 2 padx 5
deal_button.grid(row=0, column=2, padx=5)



window.mainloop()