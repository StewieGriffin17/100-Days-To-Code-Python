# A simple turtle racing game
 
from turtle import Turtle, Screen
import random
 
screen = Screen()
screen.setup(width=500, height=500)  # setting up the width and height of the screen

is_race_on = False

user_bet = screen.textinput(title="Make A Bet!!!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtle = []

for turtle_index in range(0, 6): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won!!! The {winner} turtle is the winner!")
            else:
                print(f"You lost!!! The {winner} turtle is the winner!")
       
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()