# Author: SCT (AMDG) 1/24/12
# "Rock Paper Scissors!"

def rps(p1, p2): # Defining Function and its 2 inputs
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'} # Sets the conditonals for the game
    if beats[p1] == p2: # Sets circumstances for player 1 victory, if player 1 input beats 2"player 1 won"
        return "Player 1 won!"
    if beats[p2] == p1: # Sets circumstances for player 2 victory, if player 2 input beats player 1 print "player 2 won"
        return "Player 2 won!"
    return "Draw!" # Sets circumstances for draw, print "Draw"

# Test Cases
print(rps("rock", "paper"))
print(rps("rock", "scissors"))
print(rps("paper", "scissors"))