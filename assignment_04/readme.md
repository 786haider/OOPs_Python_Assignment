Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

Explanation:
This code explain several important concepts about class variables and class methods:

The class variable bank_name is shared among all instances of the Bank class. It's defined outside any method and is accessible to all instances.
The change_bank_name() method is decorated with @classmethod, which means:

It takes cls (the class itself) as its first parameter instead of self
It can access and modify class variables using cls.bank_name
It can be called either from the class directly (Bank.change_bank_name()) or from an instance (branch1.change_bank_name())


When we change the class variable through the class method, the change is reflected in all instances, both existing and future ones.
Each instance still has its own individual instance variables (branch_location and manager), which remain unique to each instance.

This example clearly shows how class variables and class methods operate at the class level, affecting all instances collectively, unlike instance variables and methods which affect only individual instances.RetryClaude can make mistakes. Please double-check responses. 3.7 Sonnet