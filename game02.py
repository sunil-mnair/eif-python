import guessinggame

while True:
    
    choice = input("Play? (y/n):")
    if choice !='y':
        break

    # Game Starts here
    scores = guessinggame.thegame(cpoints=0,ppoints=0)

    print(guessinggame.result(scores))
    