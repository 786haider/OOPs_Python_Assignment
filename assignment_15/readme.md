15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.

Explnation:
I'll see that d.show() calls B's version of the method, not C's. This happens because:

Python uses the C3 Linearization algorithm to determine MRO
In this diamond inheritance pattern, Python follows a left-to-right approach in the inheritance list (class D(B, C))

The output will look something like:
Class B's show method

Method Resolution Order for class D:
- D
- B
- C
- A
- object

This MRO shows that when a method is called on a D object, Python first looks in D for the method. If not found, it checks B, then C, then A, and finally object (Python's base class).
The diamond problem occurs because both B and C inherit from A, creating multiple paths to A. Python's MRO ensures that:

Each class is only visited once
The relative order of parent classes is preserved
The first parent listed in the inheritance list gets priority

This is why B's version of show() is called instead of C's, even though both override A's implementation.