from turtle import Turtle

FONT = ("Courier", 90, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 155)
        self.l_player_score = 0
        self.r_player_score = 0

    def display(self):
        self.clear()
        score = f"{self.l_player_score}  {self.r_player_score}"
        self.write(score, False, ALIGNMENT, FONT)

    def give_left_player_point(self):
        self.l_player_score += 1

    def give_right_player_point(self):
        self.r_player_score += 1
