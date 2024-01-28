from turtle import Screen
from snake import Snake
from food import Food
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


def main():
    screen = Screen()
    screen_setup(screen)
    snake = Snake()
    key_events(screen, snake)
    food = Food()

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.respawn()

    screen.exitonclick()


if "__main__" == __name__:
    main()
