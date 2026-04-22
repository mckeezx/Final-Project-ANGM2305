

# Project Title: 
Blackjack: Simplified

## Demo:
[Demo video:](https://youtu.be/jq1vqQZ3rkM) 

## Github Repository:
[Github Repo: ](https://github.com/mckeezx/Final-Project-ANGM2305)

## Descrption:
There are only 4 files in this repository. Proposal.md outlines what I had planned for my project, README.md presents what I have finished. project.py is the "brain" of my code, it handles all of the blackjack logic and such. blackjack_gui.py is the physical part of my code as I can't render to terminal, so I used tkinter to display my game. 

My project is an emulation of the card game Blackjack, where players bet on their hand, trying to not go past 21. Players play against the dealer, who is made up of a couple logic functions. The game uses **ASCII cards and buttons and frames as a way to implement UI design** into something as simple as tkinter. The game in it's current state can allow the player to play a normal round of blackjack. There are a few Vegas Strip Mechanics incorporated into this version, being **surrender** (give up your hand and receive half your bet back) and **dealer peeking** (if the dealer has a natural blackjack, the round is instantly over.)

**I decided to halt my project and submit it as is as of 4/22/26**, as I believe ~1000 lines of code and a complete working game is more than enough. As ambitious as I wanted to be to add ace and card splitting, double down, and insurance, I do have 4 other month long projects assigned to me that are due before this one, and I have to manage my time wisely. 

Future areas of improvement could be that my logic and UI are not cleanly seperated. It is missing some of the mechanics I wanted to implement. My docstrings are a bit weird to read. Sometimes I would change my mind mid process. I also should have learned pygame but I like I said time is not on my side and I have 16 days to knock out 4 more projects I haven't started yet. I already knew tkinter so I just chose to stick with that. 

### Things I learnt from this project/proud I got down:
- ANSI colors 
- zip(*)
- deck shuffling
- ace logic
- the UI cards
- lambda commands (execute a function without a function)
- some more about tkinter
- window.after(4000, code) is really cool as it's basically time.sleep(x) but it will wait 4000 miliseconds and then execute a line of code which I think is really nice
- tkinter's grid system

### Relevance to ATEC fields:
This is a game, with UI aspects, logic, and replayability designed to give the player an experience akin to Vegas strip style/regular blackjack. 


