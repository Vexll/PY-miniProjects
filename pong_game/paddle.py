from turtle import Turtle

WIDTH = 1
HEIGHT = 5
MOVING_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(WIDTH, HEIGHT)
        self.penup()
        self.setheading(90)
        self.goto(position)

    def up(self):
        if self.ycor() >= 230:
            return
        self.forward(MOVING_DISTANCE)

    def down(self):
        if self.ycor() <= -230:
            return
        self.backward(MOVING_DISTANCE)
