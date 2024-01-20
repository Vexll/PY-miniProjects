from turtle import Turtle, Screen
from colors import color_list
import random


def random_color():
    return random.choice(color_list)


def hirst_painting(tur: Turtle):
    tur.hideturtle()
    for y in range(0, 500, 50):  # length = 10 -> 500/50 = 10
        tur.goto(0, y)
        for x in range(10):  # width = 10
            tur.pencolor(random_color())
            tur.dot(20)
            tur.penup()
            john.forward(50)


john = Turtle()
screen = Screen()
screen.colormode(255)
hirst_painting(john)
screen.exitonclick()
