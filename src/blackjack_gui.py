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

#display set up 
# bkg black
# fg green
# courier font
# disabled state so no typing
# display pack pady=10

#button set up
