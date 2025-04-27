 Composition
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

Explanation:
In this implementation:

The Engine class has its own properties (horsepower, fuel_type) and methods (start, stop, get_specs).
The Car class takes an Engine object during initialization (composition).
The Car class can access the Engine methods through its engine attribute.

This demonstrates composition ("has-a" relationship) rather than inheritance ("is-a" relationship). The car has an engine, rather than being a type of engine.