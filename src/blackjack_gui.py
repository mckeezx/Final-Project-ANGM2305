import tkinter as tk
from project import create_deck, deal_card, calc_score, check_blackjack, compare_hands, render_card
# this is the GUI of the project, while project.py is the brain

# COLOR TIME
# Background - Casino table green
BKG = "#35654d"
# text - gold
TEXT = "#EFBF04"
# hit - crimson red
HIT_BTN = "#7C292A"
# blue - dark blue
STAND_BTN = "#380474"
# surrender - dark yellow
SUR_BTN = "#E59B00"
# deal - dark green
DEAL_BTN = "#008153"
# button actual text - white
BTN = "#f5f5f5"
# credits - teal
CRED = "#85B4B4"


# window set up
# tk.Tk()
window = tk.Tk() #creates window
window.title("Vegas Strip Blackjack")
# 960x540
window.geometry("960x540")
# black bkg
window.configure(bg=BKG)

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

def start_game():
    """
    Starts the game by destroying the title frame.
    """
    title_frame.destroy()          

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
    for row in zip(*[render_card(c, hidden=(hide_dealer and i==0)) for i, c in enumerate(dealer_hand)]):
        board += "  ".join(row) + "\n"
        # do same for player's hand
    if hide_dealer:
        board += "Dealer's Score: ?\n"
    else:
        board += f"Dealer's Score: {calc_score(dealer_hand)}\n"
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
    Plays a new round of blackjack by dealing cards to hands
    
    
    """
    global player_hand, dealer_hand, bet # global modifies variable outside function

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    draw_board()

    if check_blackjack(player_hand):
        money_gotten = int(bet * 1.5)
        global money
        money += money_gotten
        message = f"\nBlackjack! you win ${money_gotten}!  | Money: ${money}"
        update_display(draw_board_string() + message)
        check_game_over()
        disable_buttons()
        window.after(4000, reset)

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
    deal_button.config(state="normal")
    

def enable_buttons():
    """
    Enables buttons from being pressed.
    """
    # set hit/stand/surrender button state to normal
    hit_button.config(state="normal")
    stand_button.config(state="normal")
    surrender_button.config(state="normal")
    deal_button.config(state="disabled")

def hit():
    """
    Player can draw a card
    
    Output:
    - add card to player hand
    """
    global player_hand
    player_hand.append(deal_card(deck))

    # bust checking
    # calc score > 21
    if calc_score(player_hand) > 21:
        # update display saying u bust
        update_display(draw_board_string() + f"\n\n★ You bust. Round over. -${bet} ★")
        global money
        money -= bet
        # disable buttons
        check_game_over()
        disable_buttons()
        # wait 2000 miliseconds, and then execute the function.
        window.after(2000, reset)

    # else if == 21, stand automatically
    elif calc_score(player_hand) == 21:
        stand()
    else:
        draw_board()

def surrender():
    """
    Player can surrender, getting half their money back

    Output:
    - Money bet on round divided by 2
    
    """
    global money, bet
    if len(player_hand) > 2:
        msg = "\nCan only surrender on first turn."
        update_display(draw_board_string(hide_dealer=True) + msg)
        return
    money -= bet // 2
    update_display(f"You surrendered. You keep ${bet // 2}.\nMoney: ${money}")
    disable_buttons()
    window.after(4000, reset)

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

    result = compare_hands(player_hand, dealer_hand)

    
    if result == "win":
        money += bet
        msg = f"\n\n★ You win! +${bet}  |  Money: ${money} ★"
        update_display(draw_board_string() + msg)
    elif result == "lose":
        money -= bet
        msg = f"\n\n★ You lose. -${bet}  |  Money: ${money} ★"
        update_display(draw_board_string() + msg)
        #lose, lose
        # else it's tie
    else: 
        msg = f"\n\n★ Push. You keep ${bet}  |  Money: ${money} ★"
        update_display(draw_board_string() + msg)
        # disable the buttons
    check_game_over()
    disable_buttons()
    window.after(4000, reset)
    
game_over = False

def check_game_over():
    """
    check if there's a game over.
    """
    # if money < 0, lose
    # if money > 1500, win
    # else keep playing
    global game_over
    if money <= 0:
        game_over = True
        update_display("Game Over. You're broke.")
        deal_button.config(state="disabled")
        return True
    elif money >= 1500:
        game_over = True
        update_display(f"You win! You reached ${money}.")
        deal_button.config(state="disabled")
        return True
    return False

def reset():
    """
    Reset for next round.
    """
    # delete input in bet
    if game_over:
        return
    bet_input.delete(0, "end")
    # tell player to bet again
    update_display("Place your bet and click Deal to play.")
    # make deal button clickable
    deal_button.config(state="normal")


#display set up 
display = tk.Text(
    window,
    # bkg black
    bg = BKG,
    # fg green
    fg = BTN,
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
button_frame = tk.Frame(window, bg=BKG)
# pack frame into block
button_frame.pack()
# hit button 
hit_button = tk.Button(button_frame, text="Hit", width=10, bg=HIT_BTN,
                        fg=TEXT, command=hit, relief="raised", bd=3)
# stand button
stand_button = tk.Button(button_frame, text="Stand", width=10, bg=STAND_BTN,
                          fg=TEXT, command=stand, relief="raised", bd=3)
# surrender button
surrender_button = tk.Button(button_frame, text="Surrender", width=10, bg=SUR_BTN,
                              fg="black", command=surrender, relief="raised", bd=3)
# all buttons will be their own frame with white text gray bg 
# use grid format to format them
hit_button.grid(row=0, column=0, padx=5)
stand_button.grid(row=0, column=1, padx=5)
surrender_button.grid(row=0, column=2, padx=5)

# bet input time
# black bg frame
bet_frame = tk.Frame(window, bg=BKG)
# pack it
bet_frame.pack()

# bet label black bg green fg courier font 
bet_label = tk.Label(bet_frame, text="Bet: $", bg=BKG, fg=BTN, font=("Courier", 12))
# it jsuts says "bet", nothing else
# 0,0
bet_label.grid(row=0, column=0)

# bet input same stats kinda
bet_input = tk.Entry(bet_frame, width=10, bg="gray", fg=BTN, font=("Courier", 12))
# one column down, padx5
bet_input.grid(row=0, column=1, padx=5)
# can take the code with bet_input.get()

# deal button some stats
deal_button = tk.Button(bet_frame, text="Deal", width=10, bg=DEAL_BTN,
                         fg=TEXT, command=place_bet, relief="raised", bd=3)
# column 2 padx 5
deal_button.grid(row=0, column=2, padx=5)

# title frame, black bg
# needs to be on bottom because it uses .place, which means it's generated on top of everything
title_frame = tk.Frame(window, bg=BKG)
title_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
# take up 100% of the window using relwidth and relheight (percentage based)

# give it a title
tk.Label(title_frame, text="♠ ♥ Vegas Strip Blackjack ♦ ♣",
         bg=BKG, fg=TEXT, font=("Courier", 24, "bold")).pack(pady=85)
# give it a label under it
tk.Label(title_frame, text="Starting money: $500  |  Get to $1500 to win.", 
         bg=BKG, fg=TEXT, font=("Courier", 12)).pack(pady=20)
tk.Label(title_frame, text="Created by: Zach McKee  |  ANGM2305 Final Project", 
         bg=BKG, fg=CRED, font=("Courier", 12)).pack(pady=20)
# give it a button that when clicked deletes the frame
tk.Button(title_frame, text="Start Game", width=15, bg=DEAL_BTN, fg=TEXT,
          font=("Courier", 12), command=start_game, relief="raised", bd=3).pack(pady=20)

update_display("Welcome. Place your bet and click Deal to play.")

# can use the hit/stand/surrender before even betting
disable_buttons()

window.mainloop()
# super cool