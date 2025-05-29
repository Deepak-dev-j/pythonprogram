import random
import sys
from enum import Enum

class rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    playerchoice = input("Enter the ....\n1 for Rock\n2 for Paper\n3 for Scissors\n> ")
    
    if not playerchoice.isdigit():
        print("❌ Please enter a number.")
        continue

    player = int(playerchoice)

    if player < 1 or player > 3:
        print("❌ You must enter 1, 2, or 3.")
        continue

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou choose: " + str(rps(player)).replace('rps.', '').title())
    print("Python chooses: " + str(rps(computer)).replace('rps.', '').title() + "\n")

    if (player == 1 and computer == 3) or \
       (player == 2 and computer == 1) or \
       (player == 3 and computer == 2):
        print("🎉 You win!")
    elif player == computer:
        print("🤝 Tie game")
    else:
        print("🐍 Python Wins!")

    again = input("\nPlay again?\nY for Yes\nQ to Quit\n> ")

    if again.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("BYEEEE...")
