from turtle import Turtle, Screen
import random

 
def get_turtles() -> list:
    turtles_list = []
    home_position = [(-225, -80), (-225, -40), (-225, 0), (-225, 40), (-225, 80), (-225, 120)]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for turtle_index in range(6):
        temp_tur = prepare_turtle(Turtle(), home_position[turtle_index], colors[turtle_index])
        turtles_list.append(temp_tur)
    return turtles_list


def prepare_turtle(tur: Turtle, home_pos: tuple, color):
    tur.shape("turtle")
    tur.color(color)
    tur.shapesize(1.5)
    tur.penup()
    tur.setposition(home_pos)
    tur.pendown()
    return tur


def move_turtle(tur: Turtle):
    distance = random.randint(10, 50)
    tur.forward(distance)
    return tur


def begin_race(turtles):
    i = 0
    temp_tur = turtles[0]
    while is_race_on(temp_tur.xcor()):
        temp_tur = move_turtle(turtles[i])
        i = (i + 1) % 6
    winning_color = temp_tur.pencolor()
    return winning_color


def is_race_on(distance):
    return distance < 230


def main():
    screen = Screen()
    screen.colormode(255)
    screen.setup(500, 400)
    guess = screen.textinput("make your bet", "Who will win the race? Enter a color").lower()
    turtles = get_turtles()
    winner = begin_race(turtles)
    if winner == guess:
        print("bravooo!")
    else:
        print(f"nope the winner is {winner}")
    screen.exitonclick()


if "__main__" == __name__:
    main()
