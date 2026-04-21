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
hit_button = tk.Button(button_frame, text="Hit", width=10, bg="gray", fg="white")
# stand button
stand_button = tk.Button(button_frame, text="Stand", width=10, bg="gray", fg="white")
# surrender button
surrender_button = tk.Button(button_frame, text="Surrender", width=10, bg="gray", fg="white")
# all buttons will be their own frame with white text gray bg 
# use grid format to format them
hit_button.grid(row=0, column=0, padx=5)
stand_button.grid(row=0, column=1, padx=5)
surrender_button.grid(row=0, column=2, padx=5)

window.mainloop()