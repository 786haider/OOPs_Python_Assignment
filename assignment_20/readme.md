20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

Explanation:
First, I defined a custom exception class InvalidAgeError that inherits from the built-in Exception class. This custom exception:

Takes the age value as an argument
Has a default error message
Customizes the string representation to include the provided age


Then I created the check_age(age) function that:

Checks if the age is less than 18
Raises the InvalidAgeError if the age is invalid
Returns a success message if the age is valid
