print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Asif]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

direction = input('Which way you want to go? "Left" or "Right" ').lower()
if direction == "left":
    transport = input('You reached a river. Do you want to wait or swim? ').lower()
    if transport == "wait":
        door = input("There are three doors in front of you. RED, BLUE and YELLOW. In which you want to go inside? ").lower()
        if door == "red":
            print("The room is in fire. You burned to death.")
            print("GAME OVER!!!")
        elif door == "blue":
            print("The door leads to the north pole. You froze to death.")
            print("GAME OVER!!!")
        elif door == "yellow":
            print("CONGRATULATIONS, You found the one piece!!!")
    else:
        print("You got eaten by a crocodile.")
        print("GAME OVER!!!")
else:
    print("You fell in a hole.")
    print("GAME OVER!!!")
