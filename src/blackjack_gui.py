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

def draw_board():
    """
    Render cards, show player/dealer hand, show money, your bet, score
        
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
    update_display(board)

def new_round():
    """
    Plays a new round of blackjack.
    
    
    """
    global player_hand, dealer_hand, bet # global modifies variable outside function

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    draw_board()

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
    pass


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



window.mainloop()