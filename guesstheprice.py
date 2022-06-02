import random

# Introduction to the game


def debut():
    print("Welcome to | Guess the Price |")
    print("To win, you'll have to achieve 1,000,000$!")
    print("You win 100,000 for every correct answers. You have 3 tries until you lose.")
    print("The price is between 1 & 10.")
    debut = True
    while debut:
        play = str(input("Play ? Y/N > "))
        if play == "Y":
            game()
            debut = False
        elif play == "N": 
            debut = False

# Guess the price     

def game():
    money = 0
    try1 = 4   
    price = random.randint(1 , 10)
    s = True

    while s:
        
        guess = float(input("Guess > "))

        if guess < price:
            try1 -= 1
            print("Higher! -1 Try",try1,"left.")

        if guess > price:
            try1 -= 1
            print("Lower! -1 Try",try1,"left.")

        if try1 == 0:
            lose()
            s = False
                
        if try1 == 0:
            lose()
            s = False

        if guess == price:
            print("Correct! You win:")
            
           
            s = False
            money += 100000
            print(money,"$")
            continu1 = True
            while continu1:
                print("+1 Try.")
                continu = str(input("Continue ? Y/N > "))
                if continu == "Y":
                    price = random.randint(1 , 5)
                    try1 += 1
                    continu1 = False
                    s = True

                elif continu == "N":
                    continu1 = False
     
#lose script

def lose():
    print("Oh no! You lost..")
    print("but Great Job!")
    debut()

debut()