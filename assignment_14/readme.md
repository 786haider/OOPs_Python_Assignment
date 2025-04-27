14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

Explanation:
This code demonstrates aggregation, where:

The Employee class has its own attributes and methods, existing independently.
The Department class maintains a list of references to Employee objects.
The Department can add or remove employees without affecting their existence.
If the Department object is deleted, the Employee objects continue to exist.

The key difference between aggregation and composition is that in aggregation, the contained objects can exist independently of the container. In this case, employees can exist without being part of any department, which is a classic example of aggregation.