import random

def thegame(cpoints,ppoints):
    
    for x in range(1,6):
        # Generates a random number between 1 to 5
        computer = random.randint(1,5)
        # make the user guess the number

        while True:
            try:
                player = int(input("Guess the Number:"))
            except:
                print("Enter a Number")
            else:
                if player == computer:
                    print("Won")
                    ppoints += 1
                else:
                    print(f'You Lost, the computer chose {computer}')
                    cpoints += 1
                break

    return cpoints,ppoints

def result(scores):
    # (3,2)
    if scores[0] > scores[1]:
        return f"Computer won with {scores[0]} points"
    else:
        return f"You won with {scores[1]} points"