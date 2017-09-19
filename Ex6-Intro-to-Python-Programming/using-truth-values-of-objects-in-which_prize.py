"""
Quiz: Which prize?
In this quiz, implement a function called which_prize() that notifies a competitor of the prize they
have won in a game, depending on the number of points they've scored.

Points	Prize
0 - 50	wooden rabbit
51 - 150	No prize
151 - 180	wafer-thin mint
181 - 200	penguin

The input to which_prize() will be the number of points (an integer). The function which_prize()
should return the text "Congratulations! You have won a [prize name]!" with the prize name included
if they have won a prize and the text "Oh dear, no prize this time." if there is no prize. As always,
test your function to check whether it's performing correctly.

Rewrite the which_prize() function from earlier to use what you've learned about truth values. Start
your function by setting the variable prize = None, change the prize depending on the number of
points and then use another conditional to return a message depending on whether prize is there or
not. This will avoid repeating the return part of the code.
"""

def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."