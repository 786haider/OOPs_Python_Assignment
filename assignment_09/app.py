from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    All shape classes should inherit from this class and implement the area method.
    """
    
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This method must be implemented by all subclasses.
        """
        pass
    
    def display_info(self):
        print(f"This is a {self.__class__.__name__} with area: {self.area()}")


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    Implements the required area method.
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print(f"Rectangle area: {rectangle.area()}")
    rectangle.display_info()

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        
        def area(self):
            import math
            return math.pi * self.radius ** 2
    
    circle = Circle(7)
    print(f"Circle area: {circle.area()}")
    circle.display_info()