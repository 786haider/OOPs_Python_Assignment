Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

EXplanation:
The __init__ method serves as the constructor, which is called whenever a new Logger object is created. It prints a creation message with the logger's name.
The __del__ method serves as the destructor, which is called when an object is about to be destroyed . It prints a destruction message.

Note that in Python, the destructor's execution timing is not always predictable because it depends on the garbage collector. Unlike some other languages like C++, Python's garbage collection is based on reference counting and the __del__ method might not be called immediately when an object goes out of scope.