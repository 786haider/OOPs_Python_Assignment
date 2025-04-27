17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

This demonstrates:

The class decorator add_greeting takes a class as input and returns a modified version of that class
Inside the decorator, we define a new greet() method and attach it to the class
The @add_greeting syntax applies the decorator to the Person class
After decoration, instances of Person have access to both their original methods and the added greet() method
We can verify the method is actually added to the class by checking dir(Person)

Class decorators are powerful because they can modify classes in various ways, such as adding methods/attributes, implementing mixins, or enforcing patterns across multiple classes.