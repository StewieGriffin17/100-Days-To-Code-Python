# Creating a similar artwork like Damien Hirst's famous spot paintings
import turtle
import random

color_list = [(198, 175, 117), (125, 37, 25), (209, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 53), (221, 224, 228), (108, 68, 85)]

## This list contains flashy and vibrant colors.
# color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 165, 0), (128, 0, 128), (255, 20, 147), (0, 255, 127), (255, 105, 180), (75, 0, 130), (255, 69, 0), (60, 179, 113), (238, 130, 238)]


turtle.colormode(255)
brian = turtle.Turtle()
brian.speed("fastest")
brian.hideturtle()
brian.penup()

brian.setheading(225)
brian.forward(300)
brian.setheading(0)

for i in range(1, 101):
    brian.dot(20, random.choice(color_list))
    brian.forward(50)
    if i % 10 == 0:
        brian.setheading(90)
        brian.forward(50)
        brian.setheading(180)
        brian.forward(500)
        brian.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
