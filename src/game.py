import random

options = ["Rock", "Paper", "Scissors"]


# robotRandy = random.randint(0,2)
robotRandy = 0
player = 0
win = False
draw = False
   
def choice(int):
    if int == 0:
        player = 0
    elif int == 1:
        player = 1
    else:
        player = 2


    '''
    try:
        player = int(input("Enter a number 1, 2, or 3: Rock, Paper, or Scissors? ")) - 1
    except ValueError:
        print("Did you read the fucking instructions??")
        print("Try again...")
        continue
    '''

    '''
    if player > 2:
        print("You cant do that retard, try again")
        continue
    print("You chose: " + options[player])
    print("Robot Randy chose: " + options[robotRandy])
    '''

def check():
    if robotRandy == player:
        print("Draw! Try Again...")
        draw = True

    if robotRandy == 0 & player == 2 | robotRandy == 2 & player == 0:
        if robotRandy < player:
            print("Robot Randy Wins!")
        else:
            print("Player Wins!")
            win = True

    else:
        if robotRandy > player:
            print("Robot Randy Wins!")
        else:
            print("Player Wins!")
            win = True

    
    check2 = input("Do you wish to play again? ")

    if check2.lower == "no":
        check = False

def getResults():
    return win

def getDraw():
    return draw