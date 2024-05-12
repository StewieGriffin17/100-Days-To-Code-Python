# A simple rock paper scissors game based on randomness.
import random

user_choice = int(input("What do you choose? \nType 0 for Rock, 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
options = ["Rock", "Paper", "Scissors"]
if user_choice < 0 or user_choice >= 3:
    print("Invalid input! YOU LOSE!!!")
    exit()
elif user_choice == 0 and computer_choice == 2:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Lose!")
elif user_choice == 0 and computer_choice == 1:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Lose!")
elif user_choice == 1 and computer_choice == 0:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Win!")
elif user_choice < computer_choice:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Lose!")
elif user_choice > computer_choice:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("You Win!")
elif user_choice == computer_choice:
    print(f"You choose ->\n{options[user_choice]}")
    print(f"Computer choose ->\n{options[computer_choice]}")
    print("It's a Draw!")