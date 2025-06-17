# A simple snake game using the knowledge gained so far

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Collision with wall detection
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_over = True
        scoreboard.game_over()
    
    # Collision with tail detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()
                
screen.exitonclick()
