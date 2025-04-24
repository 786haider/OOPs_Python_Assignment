The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

Explanation of super()

The Person class is the base class (parent) with a constructor that sets the name attribute.
The Teacher class inherits from Person and adds a subject attribute.
In the Teacher constructor, super().__init__(name) calls the constructor of the parent class (Person). This ensures that:

The name attribute is properly initialized by the parent class
Any initialization logic in the parent class is executed
We avoid duplicating code


The Teacher class also overrides the introduce() method and uses super().introduce() to access the parent class's version of the method.

Using super() is important because:

It maintains the inheritance chain correctly
It works properly with multiple inheritance
It prevents the need to explicitly name the parent class, making code more maintainable
If the parent class changes, you don't need to update the child class's references

The example output shows both constructors being called in sequence when creating a Teacher object, demonstrating how super() enables proper initialization through the inheritance chain.
