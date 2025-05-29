import random
import sys
from enum import Enum
class rps(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
playagain=True
while playagain:
    playerchoice=(input("enter the ....\n1 for rock \n2 for paper \n3 for scissors "))
    player=int(playerchoice)
if player < 1 or player >3:
        sys.exit("you must enter  1,2, 0r 3")
computerchoice=random.choice("123")
computer= int(computerchoice)
print("\nYou choose" +str(rps(player)).replace('rps.','').title()+".")
print("\nPython choose" +str(rps(computer)).replace('rps.','').title()+".\n")
if player ==1 and computer ==3:
    print("🎉 You win" )    
elif player ==2 and computer ==1:
    print("🎉 You win")
elif player ==3 and computer ==2:
    print("🎉 You win")
elif player == computer:
    print("TIe game")
else:
    print("🐍 Python Wins")
playagain =input("\n Play again? \n Y for Yes or \nQ Quit \n\n")
if playagain.lower()=="y":
    continue
else:
    print("\n🎉🎉🎉🎉")
    print("Thnakyou for playing\n")
    playagain=False

sys.exit("BYEEEE...")

