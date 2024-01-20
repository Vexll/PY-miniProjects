from turtle import Turtle, Screen
from colors import turtle_colors
import random

COORDINATE = ["x", "y"]


def draw_triangle(turtle: Turtle):
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)


def draw_square(turtle: Turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(tur: Turtle):
    for steps in range(10):
        tur.forward(10)
        tur.penup()
        tur.forward(10)
        tur.pendown()


def draw_different_shapes(tur: Turtle):
    # 360 / 3 = 120 -> each angle between triangle edges
    for edges in range(3, 11):
        color = random_color()
        tur.color(color)
        shape_angle = 360 / edges
        draw_certain_shape(tur, edges, shape_angle)


def random_color():
    return random.choice(turtle_colors)


def random_walk(tur: Turtle, length: int, steps: int):
    for step in range(steps):
        tur.color(random_color())
        movement = random.choice([length, -length])
        coordinate = random.choice(COORDINATE)
        if coordinate == "x":
            temp = tur.xcor() + movement  # movement part
            tur.goto(temp, tur.ycor())
        else:
            temp = tur.ycor() + movement  # movement part
            tur.goto(tur.xcor(), temp)


def draw_certain_shape(tur: Turtle, edges: int, angle: float):
    for step in range(edges):
        tur.right(angle)
        tur.forward(100)


def draw_spirograph(tur: Turtle, size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tur.color(random_color())
        tur.setheading(tur.heading() + size_of_gap)
        tur.circle(120)


tim = Turtle()
tim.shape("arrow")
tim.speed("fastest")
draw_spirograph(tim, 5)
my_screen = Screen()
my_screen.exitonclick()
