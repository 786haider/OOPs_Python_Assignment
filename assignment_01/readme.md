1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

Explanation :
I've created a Student class with:
A constructor (__init__) that uses self to initialize the name and marks attributes
A display() method that uses self to access these attributes
The self parameter is mandatory in all instance methods, including the constructor. It refers to the specific instance of the class that's being worked with.
When you create objects like student1 and student2, Python automatically passes the object as the first argument to instance methods, which is received as self.