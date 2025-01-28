import math  # Explicit import for math

class Shape:
    """
    Base class for all shapes.
    Provides an interface for area and perimeter calculations.
    """
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method.")


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)


def display_shape_info(shape):
    """
    Polymorphic function to display shape information.
    Accepts any object derived from Shape.
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

