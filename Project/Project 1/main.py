# SNAKE, WATER, GUN GAME
'''
1 - snake
-1 - water
0 - gun
'''
# computer = -1
import random

computer = random.choice([-1, 0, 1])
# print(computer)

dict = {"s":1, "w":-1, "g":0}
user = input("Enter your choice: ")
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = dict[user]
print(f"Computer choice: {reverseDict[computer]}\nYour choice: {reverseDict[you]} ")

if(computer==you):
    print("It's a draw!!")
else:
    if(computer==-1 and you==1): #water - snake 
        print("You Win!")
    elif(computer==-1  and you==0): #water - gun
        print("You Lose!")
    elif(computer==1 and you==-1): #snake - water
        print("You Lose!")
    elif(computer==1  and you==0): #snake - gun
        print("You Win!")
    elif(computer==0 and you==1): #gun - snake
        print("You Lose!")
    elif(computer==0  and you==-1): #gun - water
        print("You Win!")
    else:
        print("Something went wrong...")