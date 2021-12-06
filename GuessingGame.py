#Guessing Game

import random

def guessTheNum(secretNumber):
    print("guess a number between 1 to 20")
    for i in range(1,3):
        n=int(input("Guess The Number:"))
        if(n<secretNumber):
            print("Your Guess is too low")
        elif(n>secretNumber):
            print("Your Guess is Too High")
        else:
            break
    if(n==secretNumber):
        print("You Got the Right Guess!! ",secretNumber,"is the correct answer")
    else:
        print("Sorry! i was Guessing ",secretNumber)

while True:
    secretNumber=random.randint(1,20)
    guessTheNum(secretNumber)
    yn=input("Want to play again? y/n: ")
    if yn.lower() in 'Nn':
        break
        


                
input("Press enter to exit")
