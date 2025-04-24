 Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

Explanation:
Explanation of Python Access Modifiers
In Python, access modifiers work differently than in other languages like Java or C++. 

Public Variable (name)
Can be accessed directly from outside the class
No restrictions on access or modification
Named without any leading underscores

Protected Variable (_salary)
Indicated by a single leading underscore (_)
This is a convention only in Python - not enforced by the interpreter
Can still be accessed and modified directly, but the underscore signals to developers that this variable is intended for internal use
External code should generally avoid accessing it directly

Private Variable (__ssn)
Indicated by double leading underscores (__)
Python performs "name mangling" - the variable is renamed to _ClassName__variableName internally
When you try to access emp.__ssn directly, you'll get an AttributeError
However, you can still access it using the mangled name: emp._Employee__ssn
This is not true encapsulation but provides a basic level of hiding

Key Takeaways
Python relies on conventions rather than strict enforcement for access control
The "privacy" is more about signaling intent than creating actual barriers
Python follows the philosophy of "we're all consenting adults here" - meaning developers are trusted to respect these conventions
Private variables can still be accessed if you know the name mangling pattern
Protected and private variables are still accessible from within class methods
