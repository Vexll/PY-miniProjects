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
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.left, "Left")


def check_tail_collision(snake: Snake):
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            return True


def main():
    screen = Screen()
    screen_setup(screen)

    snake = Snake()
    key_events(screen, snake)
    food = Food()

    scoreboard = Scoreboard()
    scoreboard.display_score()

    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(0.08)
        snake.move()

        # detected collision with food
        if snake.head.distance(food) < 18:
            food.respawn()
            scoreboard.increase_score()
            snake.increase_tail()

        # detected collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290) or (
                snake.head.ycor() > 290 or snake.head.ycor() < -290):
            scoreboard.reset()
            snake.reset()

        # detected collision with tail
        if check_tail_collision(snake):
            scoreboard.reset()
            snake.reset()

    scoreboard.game_over()
    scoreboard.set_high_score()
    scoreboard.play_again()

    screen.exitonclick()


if __name__ == "__main__":
    main()
