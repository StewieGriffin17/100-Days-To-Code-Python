import random

logo = """
  ______                               _              ______  _     _ ______  ______  _______ ______  
 / _____)                         _   | |            |  ___ \| |   | |  ___ \(____  \(_______|_____ \ 
| /  ___ _   _  ____  ___  ___   | |_ | | _   ____   | |   | | |   | | | _ | |____)  )_____   _____) )
| | (___) | | |/ _  )/___)/___)  |  _)| || \ / _  )  | |   | | |   | | || || |  __  (|  ___) (_____ ( 
| \____/| |_| ( (/ /|___ |___ |  | |__| | | ( (/ /   | |   | | |___| | || || | |__)  ) |_____      | |
 \_____/ \____|\____|___/(___/    \___)_| |_|\____)  |_|   |_|\______|_||_||_|______/|_______)     |_|
"""
congratulation = """
   ___                            _         _       _   _             
  / __\___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  
 / /  / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \ 
/ /__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | |
\____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|
                  |___/                                               
"""
lost = """
                    __           _   
/\_/\___  _   _    / /  ___  ___| |_ 
\_ _/ _ \| | | |  / /  / _ \/ __| __|
 / \ (_) | |_| | / /__| (_) \__ \ |_ 
 \_/\___/ \__,_| \____/\___/|___/\__|
                                     
"""

print(logo)
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

match difficulty:
  case 'easy':
    attempts = 10
    while attempts > 0:
      print(f"You have {attempts} attempts remainging to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == number:
        print(congratulation)
        print("You guessed the number correctly.")
        break
      elif guess > number :
        print("Too high!")
        attempts = attempts-1
      elif guess < number :
        print("Too low!")
        attempts = attempts - 1
      if attempts == 0:
        print(lost)
        print("No more attempts left.")
      
  case 'hard':
    attempts = 5
    while attempts > 0:
      print(f"You have {attempts} attempts remainging to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == number:
        print(congratulation)
        print("You guessed the number correctly.")
        break
      elif guess > number :
        print("Too high!")
        attempts = attempts-1
      elif guess < number :
        print("Too low!")
        attempts = attempts - 1
      if attempts == 0:
        print(lost)
        print("No more attempts left.")
        
  case _:
    print("Wrong input!")