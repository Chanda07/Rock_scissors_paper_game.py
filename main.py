import random


def Winner(pc,player):
    if pc == player:
        return None
    elif pc == "r":
        if player == "s":
            return False
        elif player == "p":
            return True
    elif pc == "s":
        if player == "p":
            return False
        elif player == "r":
            return True
    elif pc == "p":
        if player == "r":
            return False
        elif player == "s":
            return True

print("Computer Turn: Choose Rock(r), Scissors(s) or Paper(p)? ")

randomNo = random.randint(1,3) 
if randomNo == 1:
    pc = "r"
elif randomNo == 2:
    pc = "s"
elif randomNo == 3:
    pc = "p"

player = input("Your Turn: Choose Rock(r), Scissors(s) or Paper(p)? : ")

    
game = Winner(pc,player)

print("Computer chose: ",pc)
print("You chose: ",player)

if game == None:
    print("Tie!!!!")
elif game == True:
    print("You Win !!!")
elif game == False:
    print("You Lose!!!")