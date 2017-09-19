'''Quiz: Which prize?
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
'''
def which_prize(points):
    if points < 51:
            prize = 'wooden rabbit'
    elif points > 50 and points < 151:
            return "Oh dear, no prize this time."
    elif points > 151 and points < 181:
            prize = 'wafer-thin mint'
    else:
            prize = 'penguin'
    return "Congratulations! You have won a {}!".format(prize)

print(which_prize(10))
print(which_prize(55))
print(which_prize(164))
print(which_prize(190))

'''Udacity solution:
def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"
'''