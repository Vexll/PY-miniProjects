from turtle import Turtle, Screen


class Pen:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def get_color(self):
        return self.color


def print_pen_properties(pens):
    for pen in pens:
        print(f"Color: {pen.get_color()}, Brand: {pen.brand}")


alphabets = ['a', 'b', 'c']
for i, letter in enumerate(alphabets):
    print(i)
    print(letter)
