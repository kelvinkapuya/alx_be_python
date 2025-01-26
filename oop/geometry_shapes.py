import math

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

