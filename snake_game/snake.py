from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        temp = 0
        for pos in STARTING_POSITION:
            new_segment = Turtle("square")
            if temp == 0:
                new_segment.color("red")
                temp += 1
            else:
                new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def increase_tail(self):
        new_segment = self.segments[-1].clone()
        self.segments.append(new_segment)
