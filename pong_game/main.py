from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLES_POSITION = [(350, 0), (-350, 0)]
END_SCORE = 3


def is_there_collision(paddle: Paddle, ball: Ball):
    return ball.distance(paddle) < 45 and (ball.xcor() > 320 or ball.xcor() < -320)


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle(PADDLES_POSITION[0])
    left_paddle = Paddle(PADDLES_POSITION[1])
    scoreboard = Scoreboard()
    ball = Ball()

    screen.listen()
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")
    game_is_on = True
    winner = ""
    while game_is_on:
        screen.update()
        scoreboard.display()
        ball.move()
        time.sleep(ball.move_speed)

        # detect collision with wall
        if ball.ycor() > 285 or ball.ycor() < -285:
            ball.bounce_y()

        # detect collision with r_paddle
        if is_there_collision(right_paddle, ball) or is_there_collision(left_paddle, ball):
            ball.bounce_x()

        # detect if left player score a goal
        if ball.xcor() > 400:
            scoreboard.give_left_player_point()
            ball.reset()

        # detect if right player score a goal
        if ball.xcor() < -400:
            scoreboard.give_right_player_point()
            ball.reset()

        # detect the winner and end the game
        if scoreboard.l_player_score == END_SCORE:
            winner = "left_player"
            game_is_on = False

        if scoreboard.r_player_score == END_SCORE:
            winner = "right_player"
            game_is_on = False

    scoreboard.display()
    print(f"congratulation for {winner}")
    screen.exitonclick()


if __name__ == "__main__":
    main()
