from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def screen_setup(screen: Screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)  # 0 = turn off


def key_events(screen, snake):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")


def check_tail_collision(snake: Snake):
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            return True


def main():
    screen = Screen()
    screen_setup(screen)

    scoreboard = Scoreboard()
    scoreboard.display_score()

    snake = Snake()
    key_events(screen, snake)

    food = Food()

    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detected collision with food
        if snake.head.distance(food) < 15:
            food.respawn()
            scoreboard.increase_score()
            scoreboard.display_score()
            snake.increase_tail()

        # detected collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290) or (
                snake.head.ycor() > 290 or snake.head.ycor() < -290):
            is_game_on = False

        # detected collision with tail
        if check_tail_collision(snake):
            is_game_on = False

    scoreboard.game_over()
    screen.exitonclick()


if "__main__" == __name__:
    main()
