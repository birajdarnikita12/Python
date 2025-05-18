# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():
    print("You are playing a game..")
    score = random.randint(1,64)
    # fetch the hiscore
    with open("N:/Tech/Python/Practice Set/CHAPTER 9 - PS/Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score : {score}")
    if(score>hiscore):
        with open("N:/Tech/Python/Practice Set/CHAPTER 9 - PS/Hi-score.txt", "w") as f:
            f.write(str(score))
    return score
game()