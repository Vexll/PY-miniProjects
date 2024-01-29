from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")
END_GAME_FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 265)
        self.score = 0

    def display_score(self):
        self.clear()
        text = f"Score: {self.score}"
        self.write(text, False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, ALIGNMENT, END_GAME_FONT)
