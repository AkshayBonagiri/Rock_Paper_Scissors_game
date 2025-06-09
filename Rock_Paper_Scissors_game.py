import random

# Dictionary to map numbers to choices
game = {1: "Rock", 2: "Paper", 3: "Scissor"}
# Reverse dictionary to map choices to numbers
revgame = {"Rock": 1, "Paper": 2, "Scissor": 3}

# Randomly select the computer's choice as a number
computer = random.choice([1, 2, 3])

# Take user input and standardize the case to match the keys in revgame
user = input("Choose: ").capitalize()

# Convert user choice from string to number using revgame
userchoice = revgame[user]

# Show both choices
print(f"You choose {user} and the computer choose {game[computer]}")

# Check for a draw
if userchoice == computer:
    print("Its a draw!")

# Check all win/lose conditions
else:
    if userchoice == 1 and computer == 2:
        print("You Lost!")
    elif userchoice == 1 and computer == 3:
        print("You Won!")
    elif userchoice == 2 and computer == 1:
        print("You Won!")
    elif userchoice == 2 and computer == 3:
        print("You lost!")
    elif userchoice == 3 and computer == 1:
        print("You lost!")
    elif userchoice == 3 and computer == 2:
        print("You Won!")
    else:
        # Fallback for unexpected input (shouldn't occur)
        print("Something went wrong:(")





