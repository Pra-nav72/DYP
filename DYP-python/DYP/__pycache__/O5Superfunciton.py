# super(): used in child class to call the function of parent class
#       Allows you to extend the functionality of the inherited method

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("Red", True, 7)
square = Square("Blue", False, 12)
triangle = Triangle("Yellow", True, 10, 6)

def display(shape):
    print(f"color is:  {shape.color}")
    print(f"is shape filled: {shape.is_filled}")
    if shape is circle:
        print(f"radius of the shape: {shape.radius}cm")
    elif shape is square:
        print(f"width of the shape is: {shape.width}cm")
    else:
        print(f"width X height of shape is: {shape.width} X {shape.height}")

display(circle)
display(square)
display(triangle)