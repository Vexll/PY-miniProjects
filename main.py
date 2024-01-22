class Pen:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def get_color(self):
        return self.color


def print_pen_properties(pens):
    for pen in pens:
        print(f"Color: {pen.get_color()}, Brand: {pen.brand}")


# Example usage
pen_list = [Pen("Blue", "Brand A"), Pen("Red", "Brand B"), Pen("Green", "Brand C")]
print_pen_properties(pen_list)
