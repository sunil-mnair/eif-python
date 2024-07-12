# Random Number Game
import random

while True:
    
    choice = input("Play? (y/n):")
    if choice !='y':
        break

    # Game Starts here
    ppoints=0
    cpoints=0




    # The game should run for 5 rounds
    for x in range(1,6):
        # Generates a random number between 1 to 5
        computer = random.randint(1,5)
        # make the user guess the number
        player = int(input("Guess the Number:"))

        if player == computer:
            print("Won")
            ppoints += 1
        else:
            print(f'You Lost, the computer chose {computer}')
            cpoints += 1


    # display final points at the end of the game
    if ppoints > cpoints:
        print(f"You won with {ppoints} points")
    else:
        print(f"You lost with just {ppoints} points")




