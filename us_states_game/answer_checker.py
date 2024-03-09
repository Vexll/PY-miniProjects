from turtle import Turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")
TEXT_MOVE = False


class AnswerChecker(Turtle):

    def __init__(self):
        super().__init__()
        self.data = pd.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.x_cors = self.data.x.to_list()
        self.y_cors = self.data.y.to_list()
        self.user_score = 0

    def check_answer(self, user_answer: str):
        for index, state in enumerate(self.all_states):
            if user_answer.lower() == state.lower():
                self.increase_score()
                self.place_state(index, state)
                self.update_date(index)

    def place_state(self, index: int, state_name: str):
        x = self.x_cors[index]
        y = self.y_cors[index]
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.color("black")
        state.goto(x, y)
        state.write(state_name, TEXT_MOVE, align=ALIGNMENT, font=FONT)

    # this function remove the correct date that entered by user
    def update_date(self, index: int):
        self.all_states.pop(index)
        self.x_cors.pop(index)
        self.y_cors.pop(index)

    def increase_score(self):
        self.user_score += 1
