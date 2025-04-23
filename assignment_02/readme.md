2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

Explanation:
I've created a Counter class with a class variable count initialized to 0.
The __init__ method increments the count whenever a new object is instantiated.
I've added two class methods that use the cls parameter:

display_count(): Returns the current count of objects created
reset_count(): Resets the counter to zero
The cls parameter allows these methods to access and modify the class's attributes directly, without needing an instance.
The example usage demonstrates creating objects and viewing the counter at different points.

The key difference between self and cls:

self refers to an instance of the class
cls refers to the class itself, allowing operations on class-level variables and methods
