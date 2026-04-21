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
display = tk.Text(
# bkg black
bg = "black",
# fg green
fg = "green",
# courier font
font=("Courier", 12),
# disabled state so no typing
state = "disabled"
width = 100
height = 100
)
# display pack pady=10
display.pack(pady=10) # 10 pixel padding top and bottom

#button set up
# tk.Frame, same bg
button_frame = tk.Frame(window, bg="black")
# pack frame into block
button_frame.pack()
# hit button 
hit_button = tk.Button(button_frame, text="Hit", width=10, bg="gray", fg="white")
# stand button
stand_button = tk.Button(button_frame, text="Stand", width=10, bg="gray", fg="white")
# surrender button
surrender_button = tk.Button(button_frame, text="Surrender", width=10, bg="gray", fg="white")
# all buttons will be their own frame with white text gray bg 
# use grid format to format them