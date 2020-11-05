import random
from time import sleep

choices = ["Charmender","Squirtle","Bulbasaur"]

computer = random.choice(choices)

player = False

name = input("Hello, Please enter your Name: ")

while player == False:
    print(f"Hello, {name} Welcome to Pokemon Battles Game!!")
    player = input("Which Pokemon do you want to Choose?\n'Charmender':'Charmender'\n'Squirtle':'Squirtle'\n'Bulbasaur': 'Balbasaur'")
    if player == computer:
        print("Tie!!")
    elif player == "Charmender":
        if computer == "Squirtle":
            print("\nPlease Wait , We are loading your Results.....")
            sleep(2)
            print("You Lose!!")
        else:
            print("\nPlease Wait , We are loading your Results")
            sleep(2)
            print("You Win!!")
    elif player == "Squirtle":
        if computer == "Bulbasaur":
            print("\nPlease Wait , We are loading your Results")
            sleep(2)
            print("You Lose!!")
        else:
            print("\nPlease Wait , We are loading your Results")
            sleep(2)
            print("You Win!!")
    elif player == "Bulbasaur":
        if computer == "Charmender":
            print("\nPlease Wait , We are loading your Results")
            sleep(2)
            print("You Lose!!")
        else:
            print("\nPlease Wait , We are loading your Results")
            sleep(2)
            print("You Win!!")
    elif player == "Stop":
        print("Thanks for Playing!!")
        break
    else:
        print("That's not a Valid Play!!")


    player = False
