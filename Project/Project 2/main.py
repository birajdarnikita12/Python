# THE PERFECT GUESS

import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    guesses+=1
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")

print(f"You have guessed the number {n} correctly in {guesses} attempt.")

