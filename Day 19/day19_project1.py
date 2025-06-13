# A simple Etch-A-Sketch app

from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)
    
def move_right():
    tom.right(10)
    
def move_left():
    tom.left(10)

def clear_screen():
    tom.clear() 
    tom.penup()
    tom.home()
    tom.pendown() 

screen.listen()
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()