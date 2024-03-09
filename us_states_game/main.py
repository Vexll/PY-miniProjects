
from turtle import Screen
from answer_checker import AnswerChecker


def main():
    screen = Screen()
    screen.setup(725, 490)
    screen.title("Name the States")
    screen.bgpic("blank_states_img.gif")
    screen.tracer(0)
    checker = AnswerChecker()
    checker.hideturtle()

    is_game_on = True
    while is_game_on:
        screen.update()
        user_answer = screen.textinput(title=f"{checker.user_score}/50 States Correct",prompt="What's another state's name?")
        checker.check_answer(user_answer)

        # check when game finished
        if checker.user_score == 50:
            is_game_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
