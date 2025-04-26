Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

Explanation:

My code demonstrates the key concepts of abstract classes and methods in Python:

I import ABC (Abstract Base Class) and abstractmethod decorator from the abc module.
The Shape class is defined as an abstract base class by inheriting from ABC.
The area() method is marked as abstract using the @abstractmethod decorator, which means:

It doesn't need to have an implementation in the base class
Any subclass must implement this method
You cannot instantiate the abstract class directly

The Rectangle class inherits from Shape and properly implements the area() method.
The example includes a concrete method (display_info()) in the abstract class to show that abstract classes can contain both abstract and concrete methods.

