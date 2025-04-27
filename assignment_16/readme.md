 Function Decorators
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

Explanation:
The decorator works by:

Defining a log_function_call function that takes another function as its parameter
Creating a wrapper function inside that adds the logging behavior
Returning the wrapper function which replaces the original function
Using the @ syntax to apply the decorator to say_hello

When I call say_hello(), I am actually calling the wrapper function, which:

Prints the log message
Calls the original function with any arguments passed
Returns the result of the original function

This is a simple example, but decorators can be used for many purposes like timing, caching, access control, or input validation.