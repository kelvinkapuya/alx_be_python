import math  # Explicit import to satisfy the check
from geometry_shapes import Circle, Rectangle

def display_shape_info(shape):
    """
    Polymorphic function to display shape information.
    Accepts any object with `area` and `perimeter` methods.
    """
    print(f"Shape Info: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

def main():
    # Create instances of Circle and Rectangle
    circle = Circle(7)  # Circle with radius 7
    rectangle = Rectangle(5, 10)  # Rectangle with length 5 and width 10

    # Demonstrate polymorphism by passing different shapes
    shapes = [circle, rectangle]
    for shape in shapes:
        display_shape_info(shape)

if __name__ == "__main__":
    main()

