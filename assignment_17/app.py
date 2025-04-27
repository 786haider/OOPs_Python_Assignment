def add_greeting(cls):
    """
    A class decorator that adds a greet() method to the decorated class.
    """
    # Define the method to be added
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the method to the class
    cls.greet = greet
    
    # Return the modified class
    return cls


@add_greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old."


# Test the decorated class
if __name__ == "__main__":
    # Create a Person instance
    person = Person("Alice", 30)
    
    # Access the original method
    print(person.introduce())
    
    # Access the method added by the decorator
    print(person.greet())
    
    # Verify the greet method is now part of the Person class
    print(f"'greet' method exists in Person: {'greet' in dir(Person)}")