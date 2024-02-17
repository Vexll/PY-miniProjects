from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")
END_GAME_FONT = ("Courier", 15, "bold")
PLAY_AGAIN_FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 265)
        self.score = 0
        self.high_score = 0

    def display_score(self):
        self.clear()
        text = f"Score: {self.score}    High Score: {self.high_score}"
        self.write(text, False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def set_high_score(self):
        self.high_score = self.score
        self.score = 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, ALIGNMENT, END_GAME_FONT)

    def play_again(self):
        self.goto(0, 30)
        self.write("Press space to play again", False, ALIGNMENT, PLAY_AGAIN_FONT)
