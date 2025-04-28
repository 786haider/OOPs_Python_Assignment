21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

EXplanation:

I've created a Countdown class that implements the iterator protocol in Python by defining both the __iter__() and __next__() methods. 
Class Explanation:

__init__(self, start):
Initializes the countdown with a starting number
Stores both the initial value and the current value


__iter__(self):
Returns the iterator object (self)
Resets the current counter to the start value each time a new iteration begins
This allows us to reuse the same Countdown object for multiple iterations


__next__(self):
The core logic of the iterator
Returns the current value, then decrements it for the next call
When the counter goes below 0, raises StopIteration to signal the end of iteration
This exception is caught automatically by for loops to terminate the loop



Examples Included:

Basic for loop: Shows how the countdown works in a standard for loop
Converting to list: Demonstrates that the iterator works with Python's built-in list constructor
Multiple iterations: Shows how the same Countdown object can be used for multiple iterations