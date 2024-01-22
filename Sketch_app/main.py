from turtle import Turtle, Screen


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.left(30)


def turn_right():
    tim.right(30)


def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

tim = Turtle()
screen = Screen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
