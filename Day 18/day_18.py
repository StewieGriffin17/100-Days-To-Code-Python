from turtle import Turtle, Screen
import random

brian = Turtle()
brian.shape("triangle")
brian.color("crimson")

# # drawing a square
# for _ in range(4):
#     brian.forward(100)
#     brian.right(90)

# # drawing a dashed line
# for _ in range(10):
#     brian.forward(10)
#     brian.penup()
#     brian.forward(10)
#     brian.pendown()


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    brian.color(r, g, b)
    

def draw_shape(sides, angle):
    change_color()
    for _ in range(sides):
        brian.right(angle)
        brian.forward(100)


# # Drawing 8 shapes 
# for i in range(3, 11):
#     sides = i
#     angle = 360 / i
#     draw_shape(sides, angle)


# direction = [0, 90, 180, 270]
# brian.pensize(1)
brian.speed("fastest")

# # random walk
# for _ in range(100):
#     change_color()
#     brian.forward(30)
#     brian.setheading(random.choice(direction))

# draw a spirograph
for _ in range(50):
    change_color()
    brian.circle(100)
    brian.left(7)

screen = Screen()
screen.exitonclick()
